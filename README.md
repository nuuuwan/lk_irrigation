# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_13:15:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,605 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 13:15:58 | Thawalama (Gin Ganga) | 2.51 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-05-14 13:14:53 | Magura (Kalu Ganga) | 4.33 | 🟡 Alert | 0.025 | 🔺 Rising |
| 2026-05-14 13:12:38 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-14 13:12:10 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:10:43 | Putupaula (Kalu Ganga) | 2.70 | 🟢 Normal | -0.046 |  |
| 2026-05-14 13:08:32 | Panadugama (Nilwala Ganga) | 4.03 | 🟢 Normal | -0.040 |  |
| 2026-05-14 13:08:12 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-14 13:07:52 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:06:12 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-05-14 13:06:06 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:05:57 | Ellagawa (Kalu Ganga) | 8.23 | 🟢 Normal | -0.010 |  |
| 2026-05-14 13:05:53 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:05:23 | Rathnapura (Kalu Ganga) | 4.10 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-14 13:04:32 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-05-14 13:04:12 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-14 13:04:06 | Dunamale (Aththanagalu Oya) | 2.80 | 🟢 Normal | -0.058 |  |
| 2026-05-14 13:04:02 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 13:03:53 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-05-14 13:03:53 | Thanthirimale (Malwathu Oya) | 3.28 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:03:41 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:03:35 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-05-14 13:03:29 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | -0.031 |  |
| 2026-05-14 13:03:26 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | -0.021 |  |
| 2026-05-14 13:03:06 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:03:01 | Katharagama (Menik Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:02:59 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:02:50 | Thanamalwila (Kirindi Oya) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-05-14 13:02:43 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-14 13:02:33 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-14 13:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.41 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-14 13:02:23 | Galgamuwa (Mee Oya) | 2.28 | 🟢 Normal | -0.083 |  |
| 2026-05-14 13:02:05 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:01:55 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:01:29 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:01:20 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.030 |  |
| 2026-05-14 13:00:57 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:00:44 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-14 13:00:13 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.020 |  |
| 2026-05-14 13:00:07 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 13:14:53 | Magura (Kalu Ganga) | 4.33 | 🟡 Alert | 0.025 | 🔺 Rising |
| 2026-05-14 13:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.41 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-14 13:15:58 | Thawalama (Gin Ganga) | 2.51 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-05-14 13:03:35 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-05-14 13:06:12 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-05-14 13:02:33 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-14 13:05:23 | Rathnapura (Kalu Ganga) | 4.10 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-14 13:04:12 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-14 13:02:43 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-14 13:00:44 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-14 13:12:38 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-14 13:04:02 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 13:07:52 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:00:57 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:02:05 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:03:41 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:02:59 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:03:06 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:06:06 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:05:53 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:03:01 | Katharagama (Menik Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:03:53 | Thanthirimale (Malwathu Oya) | 3.28 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:12:10 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:01:29 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:01:55 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-14 13:05:57 | Ellagawa (Kalu Ganga) | 8.23 | 🟢 Normal | -0.010 |  |
| 2026-05-14 13:08:12 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-14 13:04:32 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-05-14 13:03:53 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-05-14 13:00:07 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-05-14 13:02:50 | Thanamalwila (Kirindi Oya) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-05-14 13:00:13 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.020 |  |
| 2026-05-14 13:03:26 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | -0.021 |  |
| 2026-05-14 13:01:20 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.030 |  |
| 2026-05-14 13:03:29 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | -0.031 |  |
| 2026-05-14 13:08:32 | Panadugama (Nilwala Ganga) | 4.03 | 🟢 Normal | -0.040 |  |
| 2026-05-14 13:10:43 | Putupaula (Kalu Ganga) | 2.70 | 🟢 Normal | -0.046 |  |
| 2026-05-14 13:04:06 | Dunamale (Aththanagalu Oya) | 2.80 | 🟢 Normal | -0.058 |  |
| 2026-05-14 13:02:23 | Galgamuwa (Mee Oya) | 2.28 | 🟢 Normal | -0.083 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)