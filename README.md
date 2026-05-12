# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_19:10:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,043 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 19:10:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.12 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-05-12 19:09:23 | Rathnapura (Kalu Ganga) | 3.05 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-05-12 19:08:54 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-12 19:07:30 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-05-12 19:07:02 | Thawalama (Gin Ganga) | 3.49 | 🟢 Normal | -0.473 |  |
| 2026-05-12 19:07:01 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-12 19:05:56 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-12 19:05:12 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 19:04:45 | Glencourse (Kelani Ganga) | 10.38 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-12 19:04:44 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-12 19:04:14 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | -0.010 |  |
| 2026-05-12 19:04:05 | Katharagama (Menik Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-05-12 19:03:43 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-05-12 19:03:27 | Thaldena (Mahaweli Ganga) | 1.90 | 🟢 Normal | 1.201 | 🔺 Rising |
| 2026-05-12 19:03:07 | Ellagawa (Kalu Ganga) | 5.47 | 🟢 Normal | -0.030 |  |
| 2026-05-12 19:02:59 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-12 19:02:56 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-12 19:02:22 | Kuda Oya (Kirindi Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-05-12 19:02:17 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 19:02:13 | Moragaswewa (Deduru Oya) | 1.80 | 🟢 Normal | -0.072 |  |
| 2026-05-12 19:02:11 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-12 19:01:41 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.105 |  |
| 2026-05-12 19:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-12 19:01:40 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 19:01:23 | Panadugama (Nilwala Ganga) | 3.86 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-05-12 19:01:19 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-12 19:01:01 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-12 19:00:36 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.083 |  |
| 2026-05-12 19:00:32 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-12 19:00:30 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 19:00:15 | Nakkala (Kumbukkan Oya) | 2.98 | 🟢 Normal | 1.311 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 19:00:15 | Nakkala (Kumbukkan Oya) | 2.98 | 🟢 Normal | 1.311 | 🔺 Rising |
| 2026-05-12 19:03:27 | Thaldena (Mahaweli Ganga) | 1.90 | 🟢 Normal | 1.201 | 🔺 Rising |
| 2026-05-12 18:03:22 | Magura (Kalu Ganga) | 3.41 | 🟢 Normal | 0.655 | 🔺 Rising |
| 2026-05-12 19:09:23 | Rathnapura (Kalu Ganga) | 3.05 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-05-12 19:03:43 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-05-12 19:07:30 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-05-12 19:04:45 | Glencourse (Kelani Ganga) | 10.38 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-12 19:10:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.12 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-05-12 19:01:23 | Panadugama (Nilwala Ganga) | 3.86 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-05-12 19:01:01 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-12 19:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-12 18:05:40 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-12 19:05:56 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-12 19:08:54 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-12 19:02:56 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-12 19:01:40 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 18:04:11 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-12 18:00:31 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 19:00:30 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 19:05:12 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 19:02:17 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 19:01:19 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-12 19:00:32 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-12 19:04:05 | Katharagama (Menik Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-05-12 19:07:01 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-12 19:04:44 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-12 19:02:22 | Kuda Oya (Kirindi Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-05-12 19:02:11 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-12 19:02:59 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-12 18:02:04 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-05-12 19:04:14 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | -0.010 |  |
| 2026-05-12 18:01:07 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-05-12 19:03:07 | Ellagawa (Kalu Ganga) | 5.47 | 🟢 Normal | -0.030 |  |
| 2026-05-12 18:02:40 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.031 |  |
| 2026-05-12 18:07:06 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.042 |  |
| 2026-05-12 19:02:13 | Moragaswewa (Deduru Oya) | 1.80 | 🟢 Normal | -0.072 |  |
| 2026-05-12 19:00:36 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.083 |  |
| 2026-05-12 19:01:41 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.105 |  |
| 2026-05-12 19:07:02 | Thawalama (Gin Ganga) | 3.49 | 🟢 Normal | -0.473 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)