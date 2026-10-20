# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--20_09:08:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,948 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 09:08:37 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:07:33 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:06:33 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:05:51 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:05:40 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:05:20 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | -0.021 |  |
| 2026-10-20 09:05:18 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:05:14 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.060 |  |
| 2026-10-20 09:05:05 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:04:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.27 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:04:39 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-10-20 09:04:29 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 09:04:09 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:03:40 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.020 |  |
| 2026-10-20 09:03:30 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | -0.031 |  |
| 2026-10-20 09:03:25 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.086 |  |
| 2026-10-20 09:03:03 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.011 |  |
| 2026-10-20 09:03:02 | Hanwella (Kelani Ganga) | 2.95 | 🟢 Normal | -0.040 |  |
| 2026-10-20 09:03:01 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:02:59 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:02:46 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.060 |  |
| 2026-10-20 09:02:46 | Ellagawa (Kalu Ganga) | 6.43 | 🟢 Normal | -0.020 |  |
| 2026-10-20 09:02:42 | Pitabeddara (Nilwala Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:02:40 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:02:31 | Rathnapura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.063 |  |
| 2026-10-20 09:02:16 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:02:09 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 09:02:08 | Panadugama (Nilwala Ganga) | 4.67 | 🟢 Normal | -0.059 |  |
| 2026-10-20 09:02:03 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:01:50 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:01:47 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-20 09:01:39 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-20 09:01:36 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.231 |  |
| 2026-10-20 09:01:19 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | -0.036 |  |
| 2026-10-20 09:01:17 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.080 |  |
| 2026-10-20 09:01:15 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:01:14 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-10-20 09:00:43 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:00:34 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.057 |  |
| 2026-10-20 09:00:32 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-20 08:23:51 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 09:05:20 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | -0.021 |  |
| 2026-10-20 09:02:09 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 09:04:29 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 09:01:50 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:00:43 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:02:03 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:03:01 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:07:33 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:02:42 | Pitabeddara (Nilwala Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:05:05 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:01:15 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:00:32 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:02:40 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:05:18 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:02:59 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:04:09 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:06:33 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:02:16 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:05:40 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:08:37 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:04:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.27 | 🟢 Normal | 0.000 |  |
| 2026-10-20 09:01:47 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-20 09:01:14 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-10-20 09:01:39 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-20 09:04:39 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-10-20 09:03:03 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.011 |  |
| 2026-10-20 09:03:40 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.020 |  |
| 2026-10-20 09:02:46 | Ellagawa (Kalu Ganga) | 6.43 | 🟢 Normal | -0.020 |  |
| 2026-10-20 09:03:30 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | -0.031 |  |
| 2026-10-20 09:01:19 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | -0.036 |  |
| 2026-10-20 09:03:02 | Hanwella (Kelani Ganga) | 2.95 | 🟢 Normal | -0.040 |  |
| 2026-10-20 09:00:34 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.057 |  |
| 2026-10-20 09:02:08 | Panadugama (Nilwala Ganga) | 4.67 | 🟢 Normal | -0.059 |  |
| 2026-10-20 09:05:14 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.060 |  |
| 2026-10-20 09:02:46 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.060 |  |
| 2026-10-20 09:02:31 | Rathnapura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.063 |  |
| 2026-10-20 09:01:17 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.080 |  |
| 2026-10-20 09:03:25 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.086 |  |
| 2026-10-20 09:01:36 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.231 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)