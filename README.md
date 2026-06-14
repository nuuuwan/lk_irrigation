# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_15:16:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **179,244 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 15:16:18 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | -0.019 |  |
| 2026-06-14 15:14:20 | Panadugama (Nilwala Ganga) | 3.69 | 🟢 Normal | -0.052 |  |
| 2026-06-14 15:13:16 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-14 15:11:18 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-14 15:08:30 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.016 |  |
| 2026-06-14 15:06:39 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-14 15:06:38 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.057 |  |
| 2026-06-14 15:06:05 | Rathnapura (Kalu Ganga) | 3.09 | 🟢 Normal | -0.063 |  |
| 2026-06-14 15:06:00 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-06-14 15:04:31 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-06-14 15:04:15 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-06-14 15:04:14 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | -0.032 |  |
| 2026-06-14 15:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.21 | 🟡 Alert | -0.042 |  |
| 2026-06-14 15:03:47 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 15:03:44 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-14 15:03:43 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-06-14 15:03:29 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-06-14 15:03:29 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | -0.073 |  |
| 2026-06-14 15:03:11 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-06-14 15:03:11 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.045 |  |
| 2026-06-14 15:03:10 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.031 |  |
| 2026-06-14 15:03:09 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | -0.030 |  |
| 2026-06-14 15:02:46 | Hanwella (Kelani Ganga) | 3.37 | 🟢 Normal | -0.051 |  |
| 2026-06-14 15:02:40 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-06-14 15:02:40 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-14 15:02:37 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-14 15:02:22 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-06-14 15:01:41 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | -0.049 |  |
| 2026-06-14 15:01:27 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-14 15:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-06-14 15:01:13 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 15:01:12 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-14 15:01:08 | Ellagawa (Kalu Ganga) | 8.17 | 🟢 Normal | -0.071 |  |
| 2026-06-14 15:00:54 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-14 15:00:34 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-06-14 15:00:27 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-14 15:00:25 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 15:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.21 | 🟡 Alert | -0.042 |  |
| 2026-06-14 15:13:16 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-14 15:03:47 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 15:02:40 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-14 15:01:12 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-14 15:01:27 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-14 15:11:18 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-14 15:01:13 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-14 15:00:34 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-06-14 15:02:37 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-14 14:02:49 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-14 15:00:27 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-14 15:00:54 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-14 15:03:44 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-14 15:02:22 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-06-14 15:06:39 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-14 15:03:11 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-06-14 15:02:40 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-06-14 14:01:17 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.010 |  |
| 2026-06-14 15:04:15 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-06-14 15:03:29 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-06-14 15:06:00 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-06-14 15:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-06-14 15:00:25 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-14 15:08:30 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.016 |  |
| 2026-06-14 15:16:18 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | -0.019 |  |
| 2026-06-14 15:04:31 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-06-14 15:03:09 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | -0.030 |  |
| 2026-06-14 15:03:43 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-06-14 15:03:10 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.031 |  |
| 2026-06-14 15:04:14 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | -0.032 |  |
| 2026-06-14 15:03:11 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.045 |  |
| 2026-06-14 15:01:41 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | -0.049 |  |
| 2026-06-14 15:02:46 | Hanwella (Kelani Ganga) | 3.37 | 🟢 Normal | -0.051 |  |
| 2026-06-14 15:14:20 | Panadugama (Nilwala Ganga) | 3.69 | 🟢 Normal | -0.052 |  |
| 2026-06-14 15:06:38 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.057 |  |
| 2026-06-14 15:06:05 | Rathnapura (Kalu Ganga) | 3.09 | 🟢 Normal | -0.063 |  |
| 2026-06-14 15:01:08 | Ellagawa (Kalu Ganga) | 8.17 | 🟢 Normal | -0.071 |  |
| 2026-06-14 15:03:29 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | -0.073 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)