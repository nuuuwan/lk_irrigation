# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--08_18:11:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **282,484 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Holombuwa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 18:11:32 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-10-08 18:10:40 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | -0.125 |  |
| 2026-10-08 18:10:30 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.026 |  |
| 2026-10-08 18:09:22 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:08:12 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:07:37 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-08 18:07:33 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.205 |  |
| 2026-10-08 18:07:06 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:07:01 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:05:47 | Holombuwa (Kelani Ganga) | 3.20 | 🟡 Alert | 2.003 | 🔺 Rising |
| 2026-10-08 18:05:44 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-08 18:04:43 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-08 18:04:14 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | -0.060 |  |
| 2026-10-08 18:04:02 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-08 18:03:40 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 18:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-08 18:03:09 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.039 |  |
| 2026-10-08 18:02:52 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.052 |  |
| 2026-10-08 18:02:44 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.344 | 🔺 Rising |
| 2026-10-08 18:02:43 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-10-08 18:02:32 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:02:30 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-08 18:02:30 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-10-08 18:02:25 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | -0.032 |  |
| 2026-10-08 18:02:23 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-08 18:02:22 | Panadugama (Nilwala Ganga) | 3.72 | 🟢 Normal | -0.023 |  |
| 2026-10-08 18:02:19 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:02:18 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.092 |  |
| 2026-10-08 18:02:14 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 18:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.98 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-10-08 18:02:08 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-08 18:02:00 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-08 18:01:52 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | -0.198 |  |
| 2026-10-08 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:01:35 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:01:25 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:01:11 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:01:06 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-10-08 18:00:11 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 18:05:47 | Holombuwa (Kelani Ganga) | 3.20 | 🟡 Alert | 2.003 | 🔺 Rising |
| 2026-10-08 18:02:44 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.344 | 🔺 Rising |
| 2026-10-08 18:02:43 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-10-08 18:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.98 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-10-08 18:05:44 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-08 18:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-08 18:02:00 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-08 18:02:23 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-08 18:04:43 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-08 18:02:08 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-08 18:04:02 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-08 18:07:37 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-08 18:02:14 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 18:03:40 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:01:35 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:00:11 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:01:11 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:01:25 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:07:01 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:02:19 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:08:12 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:02:32 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:09:22 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:07:06 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:02:30 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-08 18:11:32 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-10-08 18:02:30 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-10-08 18:01:06 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-10-08 18:02:22 | Panadugama (Nilwala Ganga) | 3.72 | 🟢 Normal | -0.023 |  |
| 2026-10-08 18:10:30 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.026 |  |
| 2026-10-08 18:02:25 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | -0.032 |  |
| 2026-10-08 18:03:09 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.039 |  |
| 2026-10-08 18:02:52 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.052 |  |
| 2026-10-08 18:04:14 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | -0.060 |  |
| 2026-10-08 18:02:18 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.092 |  |
| 2026-10-08 18:10:40 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | -0.125 |  |
| 2026-10-08 18:01:52 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | -0.198 |  |
| 2026-10-08 18:07:33 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.205 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)