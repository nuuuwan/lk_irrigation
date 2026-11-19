# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--19_23:03:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **320,440 measurements** from **39** stations.
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
| 2026-11-19 23:03:23 | Dunamale (Aththanagalu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.022 |  |
| 2026-11-19 23:02:37 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:02:32 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:02:10 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.011 |  |
| 2026-11-19 23:02:07 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.005 |  |
| 2026-11-19 23:01:54 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.032 |  |
| 2026-11-19 23:01:35 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:01:33 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:01:22 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:01:05 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:01:05 | Ellagawa (Kalu Ganga) | 4.81 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:00:59 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:00:42 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-19 23:00:38 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:00:22 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-19 23:00:22 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-11-19 22:31:05 | Panadugama (Nilwala Ganga) | 3.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 23:00:22 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-11-19 23:00:22 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-19 22:03:49 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-19 22:02:27 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-19 22:02:25 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-19 23:00:42 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-19 22:04:15 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-19 18:00:52 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:01:05 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:01:22 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:00:38 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:01:35 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:02:32 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-19 22:02:21 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-19 22:01:10 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:01:05 | Ellagawa (Kalu Ganga) | 4.81 | 🟢 Normal | 0.000 |  |
| 2026-11-19 22:31:05 | Panadugama (Nilwala Ganga) | 3.31 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-19 22:03:18 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:03:23 | Dunamale (Aththanagalu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:02:37 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-19 22:08:13 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-19 18:01:52 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:01:33 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-19 22:11:53 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-19 22:01:33 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:00:59 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:02:07 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.005 |  |
| 2026-11-19 22:09:12 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-11-19 18:05:17 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-11-19 21:04:45 | Moraketiya (Walawe Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-11-19 22:02:41 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-19 23:02:10 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.011 |  |
| 2026-11-19 22:04:14 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.019 |  |
| 2026-11-19 22:06:22 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-19 23:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.022 |  |
| 2026-11-19 23:01:54 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.032 |  |
| 2026-11-19 22:07:17 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | -0.034 |  |
| 2026-11-19 22:05:53 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)