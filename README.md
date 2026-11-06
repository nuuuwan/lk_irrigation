# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_09:03:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,261 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 09:03:41 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:03:29 | Moragaswewa (Deduru Oya) | 2.94 | 🟢 Normal | -0.022 |  |
| 2026-11-06 09:03:04 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-06 09:02:54 | Ellagawa (Kalu Ganga) | 6.13 | 🟢 Normal | -0.019 |  |
| 2026-11-06 09:02:44 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:02:40 | Thanamalwila (Kirindi Oya) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-11-06 09:02:25 | Thaldena (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.338 |  |
| 2026-11-06 09:02:10 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-11-06 09:01:44 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-11-06 09:01:28 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:01:09 | Giriulla (Maha Oya) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-11-06 09:01:00 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-11-06 09:00:49 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:00:27 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.060 |  |
| 2026-11-06 09:00:25 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-06 08:49:16 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-11-06 08:25:13 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 08:06:56 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-11-06 09:02:10 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-11-06 08:09:35 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-06 09:03:04 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-06 09:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:00:49 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:01:28 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-11-06 08:08:13 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:03:41 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-06 08:05:58 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:02:44 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-06 08:09:15 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-06 08:04:02 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-11-06 08:02:01 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-11-06 08:02:08 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-11-06 08:03:36 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-11-06 09:01:44 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-11-06 09:00:25 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-06 08:01:59 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-06 08:01:46 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-11-06 08:13:35 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | -0.011 |  |
| 2026-11-06 08:49:16 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-11-06 09:02:54 | Ellagawa (Kalu Ganga) | 6.13 | 🟢 Normal | -0.019 |  |
| 2026-11-06 09:01:09 | Giriulla (Maha Oya) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-11-06 09:02:40 | Thanamalwila (Kirindi Oya) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-11-06 09:01:00 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-11-06 09:03:29 | Moragaswewa (Deduru Oya) | 2.94 | 🟢 Normal | -0.022 |  |
| 2026-11-06 08:06:39 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | -0.023 |  |
| 2026-11-06 08:06:10 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | -0.030 |  |
| 2026-11-06 08:11:04 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.038 |  |
| 2026-11-06 08:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.39 | 🟢 Normal | -0.040 |  |
| 2026-11-06 08:04:48 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.049 |  |
| 2026-11-06 08:03:40 | Rathnapura (Kalu Ganga) | 2.48 | 🟢 Normal | -0.050 |  |
| 2026-11-06 08:02:56 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | -0.054 |  |
| 2026-11-06 08:08:17 | Moraketiya (Walawe Ganga) | 1.74 | 🟢 Normal | -0.059 |  |
| 2026-11-06 09:00:27 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.060 |  |
| 2026-11-06 08:06:22 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | -0.067 |  |
| 2026-11-06 08:01:04 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.071 |  |
| 2026-11-06 09:02:25 | Thaldena (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.338 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)