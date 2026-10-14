# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--14_12:18:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,632 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 12:18:13 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:10:01 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-10-14 12:08:36 | Panadugama (Nilwala Ganga) | 5.28 | 🟡 Alert | 6.308 | 🔺 Rising |
| 2026-10-14 12:07:47 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.019 |  |
| 2026-10-14 12:07:18 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 12:07:03 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | -0.029 |  |
| 2026-10-14 12:06:36 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:06:34 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:06:22 | Pitabeddara (Nilwala Ganga) | 1.83 | 🟢 Normal | -0.073 |  |
| 2026-10-14 12:04:56 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-10-14 12:04:42 | Panadugama (Nilwala Ganga) | 4.87 | 🟢 Normal | 6.308 | 🔺 Rising |
| 2026-10-14 12:04:34 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-14 12:04:23 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 12:04:16 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | -0.079 |  |
| 2026-10-14 12:03:45 | Baddegama (Gin Ganga) | 2.74 | 🟢 Normal | -0.010 |  |
| 2026-10-14 12:03:38 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:03:38 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-10-14 12:03:25 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:03:22 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:03:02 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 12:03:01 | Hanwella (Kelani Ganga) | 3.03 | 🟢 Normal | -0.050 |  |
| 2026-10-14 12:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.80 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-10-14 12:02:58 | Magura (Kalu Ganga) | 5.21 | 🟡 Alert | -0.090 |  |
| 2026-10-14 12:02:55 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:02:42 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.020 |  |
| 2026-10-14 12:02:34 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:02:25 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:02:24 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-14 12:02:17 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.020 |  |
| 2026-10-14 12:02:10 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.060 |  |
| 2026-10-14 12:02:07 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:01:58 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.030 |  |
| 2026-10-14 12:01:51 | Rathnapura (Kalu Ganga) | 3.65 | 🟢 Normal | -0.058 |  |
| 2026-10-14 12:01:45 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-14 12:01:24 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-10-14 12:01:14 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-14 12:01:06 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | -0.100 |  |
| 2026-10-14 12:00:10 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.021 |  |
| 2026-10-14 11:59:50 | Dunamale (Aththanagalu Oya) | 2.29 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 12:03:02 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 12:08:36 | Panadugama (Nilwala Ganga) | 5.28 | 🟡 Alert | 6.308 | 🔺 Rising |
| 2026-10-14 12:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.80 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-10-14 12:02:58 | Magura (Kalu Ganga) | 5.21 | 🟡 Alert | -0.090 |  |
| 2026-10-14 12:04:34 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-14 12:04:23 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 12:07:18 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 12:02:55 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:01:14 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:18:13 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:02:07 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:03:22 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:06:34 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:02:34 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:03:25 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:02:25 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:03:38 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:06:36 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:03:45 | Baddegama (Gin Ganga) | 2.74 | 🟢 Normal | -0.010 |  |
| 2026-10-14 12:02:24 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-14 12:03:38 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-10-14 12:01:24 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-10-14 12:10:01 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-10-14 12:01:45 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-14 12:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-14 12:04:56 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-10-14 12:07:47 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.019 |  |
| 2026-10-14 12:02:42 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.020 |  |
| 2026-10-14 12:02:17 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.020 |  |
| 2026-10-14 12:00:10 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.021 |  |
| 2026-10-14 12:07:03 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | -0.029 |  |
| 2026-10-14 12:01:58 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.030 |  |
| 2026-10-14 11:59:50 | Dunamale (Aththanagalu Oya) | 2.29 | 🟢 Normal | -0.031 |  |
| 2026-10-14 12:03:01 | Hanwella (Kelani Ganga) | 3.03 | 🟢 Normal | -0.050 |  |
| 2026-10-14 12:01:51 | Rathnapura (Kalu Ganga) | 3.65 | 🟢 Normal | -0.058 |  |
| 2026-10-14 12:02:10 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.060 |  |
| 2026-10-14 12:06:22 | Pitabeddara (Nilwala Ganga) | 1.83 | 🟢 Normal | -0.073 |  |
| 2026-10-14 12:04:16 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | -0.079 |  |
| 2026-10-14 12:01:06 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)