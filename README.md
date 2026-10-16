# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--16_07:10:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,256 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 07:10:22 | Magura (Kalu Ganga) | 3.77 | 🟢 Normal | -0.044 |  |
| 2026-10-16 07:09:22 | Galgamuwa (Mee Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-16 07:09:04 | Peradeniya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.146 |  |
| 2026-10-16 07:07:13 | Putupaula (Kalu Ganga) | 2.46 | 🟢 Normal | -0.037 |  |
| 2026-10-16 07:07:12 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-16 07:07:08 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.088 |  |
| 2026-10-16 07:07:05 | Thawalama (Gin Ganga) | 3.84 | 🟢 Normal | 52.941 | 🔺 Rising |
| 2026-10-16 07:07:01 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.084 |  |
| 2026-10-16 07:06:10 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 07:05:57 | Thawalama (Gin Ganga) | 2.84 | 🟢 Normal | 52.941 | 🔺 Rising |
| 2026-10-16 07:05:56 | Panadugama (Nilwala Ganga) | 6.69 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 07:05:17 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.029 |  |
| 2026-10-16 07:04:36 | Badalgama (Maha Oya) | 3.37 | 🟢 Normal | -0.010 |  |
| 2026-10-16 07:04:18 | Holombuwa (Kelani Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2026-10-16 07:04:13 | Hanwella (Kelani Ganga) | 3.72 | 🟢 Normal | -0.043 |  |
| 2026-10-16 07:03:57 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | -0.386 |  |
| 2026-10-16 07:03:38 | Giriulla (Maha Oya) | 2.04 | 🟢 Normal | -0.030 |  |
| 2026-10-16 07:03:26 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | -0.042 |  |
| 2026-10-16 07:03:20 | Dunamale (Aththanagalu Oya) | 3.66 | 🟡 Alert | -0.041 |  |
| 2026-10-16 07:03:18 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-10-16 07:03:13 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-10-16 07:02:29 | Rathnapura (Kalu Ganga) | 3.62 | 🟢 Normal | -0.029 |  |
| 2026-10-16 07:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.91 | 🟡 Alert | -0.011 |  |
| 2026-10-16 07:02:22 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-10-16 07:02:20 | Urawa (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-10-16 07:02:18 | Ellagawa (Kalu Ganga) | 7.53 | 🟢 Normal | -0.023 |  |
| 2026-10-16 07:02:16 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.030 |  |
| 2026-10-16 07:02:10 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-10-16 07:01:42 | Thalgahagoda (Nilwala Ganga) | 1.92 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 07:01:42 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-16 07:01:39 | Thanthirimale (Malwathu Oya) | 1.75 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-16 07:01:37 | Moragaswewa (Deduru Oya) | 2.48 | 🟢 Normal | -0.145 |  |
| 2026-10-16 07:01:31 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-10-16 07:00:47 | Pitabeddara (Nilwala Ganga) | 3.80 | 🟢 Normal | -0.361 |  |
| 2026-10-16 07:00:42 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-10-16 07:00:34 | Horowpothana (Yan Oya) | 1.92 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-16 07:00:29 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-16 07:00:06 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-10-16 07:00:03 | Urawa (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-10-16 06:44:30 | Galgamuwa (Mee Oya) | 2.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 07:05:56 | Panadugama (Nilwala Ganga) | 6.69 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 07:01:42 | Thalgahagoda (Nilwala Ganga) | 1.92 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 07:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.91 | 🟡 Alert | -0.011 |  |
| 2026-10-16 07:03:20 | Dunamale (Aththanagalu Oya) | 3.66 | 🟡 Alert | -0.041 |  |
| 2026-10-16 07:07:05 | Thawalama (Gin Ganga) | 3.84 | 🟢 Normal | 52.941 | 🔺 Rising |
| 2026-10-16 07:01:42 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-16 07:01:39 | Thanthirimale (Malwathu Oya) | 1.75 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-16 07:00:34 | Horowpothana (Yan Oya) | 1.92 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-16 07:07:12 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-16 07:00:29 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-16 07:09:22 | Galgamuwa (Mee Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-16 07:06:10 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 07:02:20 | Urawa (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-10-16 07:04:36 | Badalgama (Maha Oya) | 3.37 | 🟢 Normal | -0.010 |  |
| 2026-10-16 07:00:06 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-10-16 07:01:31 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-10-16 07:02:10 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-10-16 06:06:12 | Baddegama (Gin Ganga) | 3.07 | 🟢 Normal | -0.012 |  |
| 2026-10-16 07:03:18 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-10-16 07:04:18 | Holombuwa (Kelani Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2026-10-16 07:02:18 | Ellagawa (Kalu Ganga) | 7.53 | 🟢 Normal | -0.023 |  |
| 2026-10-16 06:03:11 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.025 |  |
| 2026-10-16 07:05:17 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.029 |  |
| 2026-10-16 07:02:29 | Rathnapura (Kalu Ganga) | 3.62 | 🟢 Normal | -0.029 |  |
| 2026-10-16 07:02:22 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-10-16 07:03:13 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-10-16 07:03:38 | Giriulla (Maha Oya) | 2.04 | 🟢 Normal | -0.030 |  |
| 2026-10-16 07:02:16 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.030 |  |
| 2026-10-16 07:00:42 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-10-16 07:07:13 | Putupaula (Kalu Ganga) | 2.46 | 🟢 Normal | -0.037 |  |
| 2026-10-16 07:03:26 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | -0.042 |  |
| 2026-10-16 07:04:13 | Hanwella (Kelani Ganga) | 3.72 | 🟢 Normal | -0.043 |  |
| 2026-10-16 07:10:22 | Magura (Kalu Ganga) | 3.77 | 🟢 Normal | -0.044 |  |
| 2026-10-16 07:07:01 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.084 |  |
| 2026-10-16 07:07:08 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.088 |  |
| 2026-10-16 07:01:37 | Moragaswewa (Deduru Oya) | 2.48 | 🟢 Normal | -0.145 |  |
| 2026-10-16 07:09:04 | Peradeniya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.146 |  |
| 2026-10-16 07:00:47 | Pitabeddara (Nilwala Ganga) | 3.80 | 🟢 Normal | -0.361 |  |
| 2026-10-16 07:03:57 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | -0.386 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)