# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--26_09:03:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,029 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 09:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.11 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-11-26 09:03:01 | Giriulla (Maha Oya) | 3.30 | 🟢 Normal | -0.120 |  |
| 2026-11-26 09:02:58 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | -0.080 |  |
| 2026-11-26 09:02:56 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.021 |  |
| 2026-11-26 09:02:46 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.014 |  |
| 2026-11-26 09:02:37 | Thanamalwila (Kirindi Oya) | 1.71 | 🟢 Normal | -0.030 |  |
| 2026-11-26 09:02:13 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-26 09:01:25 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-11-26 09:01:21 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 09:01:07 | Manampitiya (Mahaweli Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-11-26 09:00:23 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | -0.063 |  |
| 2026-11-26 09:00:09 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.031 |  |
| 2026-11-26 08:37:37 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | -0.039 |  |
| 2026-11-26 08:23:24 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.082 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 09:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.11 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-11-26 08:03:07 | Dunamale (Aththanagalu Oya) | 3.95 | 🟡 Alert | 0.000 |  |
| 2026-11-26 08:03:07 | Moragaswewa (Deduru Oya) | 4.07 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-11-26 08:07:30 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-26 08:04:27 | Putupaula (Kalu Ganga) | 1.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-26 08:06:01 | Badalgama (Maha Oya) | 4.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-26 09:02:13 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-26 08:13:09 | Baddegama (Gin Ganga) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 09:01:21 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 08:04:19 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-26 08:02:59 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-26 09:01:07 | Manampitiya (Mahaweli Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-11-26 08:00:35 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-11-26 09:01:25 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-11-26 09:02:46 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.014 |  |
| 2026-11-26 08:13:27 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.018 |  |
| 2026-11-26 08:04:26 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.019 |  |
| 2026-11-26 09:02:56 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-26 08:02:21 | Ellagawa (Kalu Ganga) | 6.18 | 🟢 Normal | -0.022 |  |
| 2026-11-26 08:00:46 | Wellawaya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.023 |  |
| 2026-11-26 08:03:52 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.029 |  |
| 2026-11-26 09:02:37 | Thanamalwila (Kirindi Oya) | 1.71 | 🟢 Normal | -0.030 |  |
| 2026-11-26 09:00:09 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.031 |  |
| 2026-11-26 08:37:37 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | -0.039 |  |
| 2026-11-26 08:10:18 | Holombuwa (Kelani Ganga) | 1.33 | 🟢 Normal | -0.040 |  |
| 2026-11-26 07:04:05 | Galgamuwa (Mee Oya) | 1.31 | 🟢 Normal | -0.043 |  |
| 2026-11-26 08:09:33 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | -0.047 |  |
| 2026-11-26 08:13:37 | Panadugama (Nilwala Ganga) | 3.94 | 🟢 Normal | -0.051 |  |
| 2026-11-26 08:05:36 | Rathnapura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.061 |  |
| 2026-11-26 09:00:23 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | -0.063 |  |
| 2026-11-26 09:02:58 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | -0.080 |  |
| 2026-11-26 08:23:24 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.082 |  |
| 2026-11-26 08:04:03 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.087 |  |
| 2026-11-26 08:01:50 | Weraganthota (Mahaweli Ganga) | -1.99 | 🟢 Normal | -0.101 |  |
| 2026-11-26 08:02:09 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.108 |  |
| 2026-11-26 09:03:01 | Giriulla (Maha Oya) | 3.30 | 🟢 Normal | -0.120 |  |
| 2026-11-26 08:04:13 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | -0.159 |  |
| 2026-11-26 08:07:41 | Magura (Kalu Ganga) | 3.66 | 🟢 Normal | -0.185 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)