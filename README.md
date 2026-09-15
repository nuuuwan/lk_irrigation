# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_17:03:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,720 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 17:03:49 | Hanwella (Kelani Ganga) | 2.38 | 🟢 Normal | -0.109 |  |
| 2026-09-15 17:03:41 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:03:40 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:03:38 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | -0.080 |  |
| 2026-09-15 17:03:33 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-09-15 17:03:28 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-09-15 17:02:45 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:02:39 | Putupaula (Kalu Ganga) | 1.49 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-15 17:02:26 | Panadugama (Nilwala Ganga) | 3.60 | 🟢 Normal | -0.131 |  |
| 2026-09-15 17:02:18 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-09-15 17:02:17 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-09-15 17:02:12 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.87 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:02:06 | Glencourse (Kelani Ganga) | 9.92 | 🟢 Normal | -0.141 |  |
| 2026-09-15 17:02:00 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:01:54 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:01:49 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:01:21 | Thanthirimale (Malwathu Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-09-15 17:01:14 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:01:09 | Manampitiya (Mahaweli Ganga) | -0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 17:00:09 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:26:34 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:16:35 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:16:33 | Panadugama (Nilwala Ganga) | 3.70 | 🟢 Normal | -0.131 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 16:08:35 | Magura (Kalu Ganga) | 4.47 | 🟡 Alert | -0.102 |  |
| 2026-09-15 16:05:55 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-09-15 17:02:17 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-09-15 16:08:38 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-15 16:02:51 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-15 16:09:28 | Baddegama (Gin Ganga) | 3.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-15 17:02:39 | Putupaula (Kalu Ganga) | 1.49 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-15 17:01:09 | Manampitiya (Mahaweli Ganga) | -0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 16:09:28 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:01:14 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:02:45 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:02:00 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:01:49 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:03:40 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:02:04 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:09:00 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:06:40 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:00:09 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:03:41 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:16:35 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:01:54 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:02:12 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.87 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:02:18 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-09-15 17:03:33 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-09-15 17:01:21 | Thanthirimale (Malwathu Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-09-15 16:02:56 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-09-15 16:13:07 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.018 |  |
| 2026-09-15 16:08:05 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-09-15 17:03:28 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-09-15 16:02:58 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-09-15 16:02:44 | Dunamale (Aththanagalu Oya) | 3.16 | 🟢 Normal | -0.040 |  |
| 2026-09-15 16:07:54 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.065 |  |
| 2026-09-15 17:03:38 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | -0.080 |  |
| 2026-09-15 17:03:49 | Hanwella (Kelani Ganga) | 2.38 | 🟢 Normal | -0.109 |  |
| 2026-09-15 16:05:07 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.113 |  |
| 2026-09-15 17:02:26 | Panadugama (Nilwala Ganga) | 3.60 | 🟢 Normal | -0.131 |  |
| 2026-09-15 17:02:06 | Glencourse (Kelani Ganga) | 9.92 | 🟢 Normal | -0.141 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)