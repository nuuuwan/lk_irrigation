# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--14_14:25:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,711 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 14:25:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.84 | 🟡 Alert | 0.014 | 🔺 Rising |
| 2026-10-14 14:23:28 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-14 14:16:37 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 14:14:05 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.005 |  |
| 2026-10-14 14:12:10 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | -0.009 |  |
| 2026-10-14 14:10:21 | Magura (Kalu Ganga) | 5.02 | 🟡 Alert | -0.081 |  |
| 2026-10-14 14:09:53 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.018 |  |
| 2026-10-14 14:08:23 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -0.056 |  |
| 2026-10-14 14:08:10 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.018 |  |
| 2026-10-14 14:07:27 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.075 |  |
| 2026-10-14 14:07:23 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 14:07:22 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 14:07:07 | Panadugama (Nilwala Ganga) | 5.80 | 🟡 Alert | -0.059 |  |
| 2026-10-14 14:07:06 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.020 |  |
| 2026-10-14 14:06:49 | Putupaula (Kalu Ganga) | 2.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-14 14:06:10 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 14:01:19 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 14:25:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.84 | 🟡 Alert | 0.014 | 🔺 Rising |
| 2026-10-14 14:07:07 | Panadugama (Nilwala Ganga) | 5.80 | 🟡 Alert | -0.059 |  |
| 2026-10-14 14:10:21 | Magura (Kalu Ganga) | 5.02 | 🟡 Alert | -0.081 |  |
| 2026-10-14 14:23:28 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-14 14:01:12 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-14 14:01:23 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 14:06:49 | Putupaula (Kalu Ganga) | 2.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-14 14:07:22 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 14:05:19 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 14:04:30 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-14 14:16:37 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 14:07:23 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 14:01:14 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-14 14:06:10 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-14 14:05:09 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 14:00:27 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-14 14:14:05 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.005 |  |
| 2026-10-14 14:12:10 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | -0.009 |  |
| 2026-10-14 14:05:19 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-10-14 14:04:16 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-14 14:01:14 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.010 |  |
| 2026-10-14 14:01:59 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-10-14 14:05:36 | Baddegama (Gin Ganga) | 2.72 | 🟢 Normal | -0.010 |  |
| 2026-10-14 14:02:15 | Ellagawa (Kalu Ganga) | 7.74 | 🟢 Normal | -0.010 |  |
| 2026-10-14 14:03:19 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.012 |  |
| 2026-10-14 14:00:54 | Thanthirimale (Malwathu Oya) | 0.92 | 🟢 Normal | -0.012 |  |
| 2026-10-14 14:09:53 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.018 |  |
| 2026-10-14 14:08:10 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.018 |  |
| 2026-10-14 14:04:44 | Pitabeddara (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.019 |  |
| 2026-10-14 14:03:00 | Hanwella (Kelani Ganga) | 2.94 | 🟢 Normal | -0.020 |  |
| 2026-10-14 14:07:06 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.020 |  |
| 2026-10-14 14:03:52 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-10-14 14:02:13 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | -0.021 |  |
| 2026-10-14 14:02:32 | Dunamale (Aththanagalu Oya) | 2.25 | 🟢 Normal | -0.024 |  |
| 2026-10-14 14:02:01 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.031 |  |
| 2026-10-14 14:08:23 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -0.056 |  |
| 2026-10-14 14:07:27 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.075 |  |
| 2026-10-14 14:03:39 | Rathnapura (Kalu Ganga) | 3.45 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)