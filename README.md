# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_09:30:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,284 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 09:30:22 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:14:05 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:10:21 | Dunamale (Aththanagalu Oya) | 2.33 | 🟢 Normal | -0.028 |  |
| 2026-11-06 09:09:09 | Panadugama (Nilwala Ganga) | 4.09 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:08:21 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:08:13 | Panadugama (Nilwala Ganga) | 4.09 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:08:10 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-06 09:08:09 | Weraganthota (Mahaweli Ganga) | -2.66 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-06 09:08:06 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:07:38 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:07:10 | Pitabeddara (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-11-06 09:07:01 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.032 |  |
| 2026-11-06 09:06:19 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.040 |  |
| 2026-11-06 09:06:09 | Rathnapura (Kalu Ganga) | 2.41 | 🟢 Normal | -0.067 |  |
| 2026-11-06 09:06:06 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.028 |  |
| 2026-11-06 09:05:46 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | -0.010 |  |
| 2026-11-06 09:05:40 | Moraketiya (Walawe Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:05:20 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:04:55 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | -0.031 |  |
| 2026-11-06 09:04:47 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | -0.012 |  |
| 2026-11-06 09:04:44 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:04:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.34 | 🟢 Normal | -0.049 |  |
| 2026-11-06 09:04:27 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | -0.030 |  |
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

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 09:08:09 | Weraganthota (Mahaweli Ganga) | -2.66 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-06 09:08:10 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-06 09:02:10 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-11-06 09:03:04 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-06 09:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:00:49 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:01:28 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:05:20 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:03:41 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:09:09 | Panadugama (Nilwala Ganga) | 4.09 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:05:40 | Moraketiya (Walawe Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:02:44 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:04:44 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:08:06 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:08:21 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:07:38 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:30:22 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-06 09:14:05 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-06 08:02:01 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-11-06 09:05:46 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | -0.010 |  |
| 2026-11-06 09:01:44 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-11-06 09:00:25 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-06 09:04:47 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | -0.012 |  |
| 2026-11-06 09:02:54 | Ellagawa (Kalu Ganga) | 6.13 | 🟢 Normal | -0.019 |  |
| 2026-11-06 09:01:09 | Giriulla (Maha Oya) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-11-06 09:07:10 | Pitabeddara (Nilwala Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-11-06 09:02:40 | Thanamalwila (Kirindi Oya) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-11-06 09:01:00 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-11-06 09:03:29 | Moragaswewa (Deduru Oya) | 2.94 | 🟢 Normal | -0.022 |  |
| 2026-11-06 09:06:06 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.028 |  |
| 2026-11-06 09:10:21 | Dunamale (Aththanagalu Oya) | 2.33 | 🟢 Normal | -0.028 |  |
| 2026-11-06 09:04:27 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | -0.030 |  |
| 2026-11-06 09:04:55 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | -0.031 |  |
| 2026-11-06 09:07:01 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.032 |  |
| 2026-11-06 09:06:19 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.040 |  |
| 2026-11-06 09:04:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.34 | 🟢 Normal | -0.049 |  |
| 2026-11-06 09:00:27 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.060 |  |
| 2026-11-06 09:06:09 | Rathnapura (Kalu Ganga) | 2.41 | 🟢 Normal | -0.067 |  |
| 2026-11-06 09:02:25 | Thaldena (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.338 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)