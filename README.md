# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--15_12:12:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **46,222 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 12:12:15 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-01-15 12:12:01 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-15 12:09:55 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:08:49 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:08:16 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:07:18 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.038 |  |
| 2026-01-15 12:05:32 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:05:20 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:04:34 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:04:34 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.021 |  |
| 2026-01-15 12:04:09 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:04:01 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.030 |  |
| 2026-01-15 12:03:54 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-15 12:03:51 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.039 |  |
| 2026-01-15 12:03:40 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:03:29 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:03:21 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:03:00 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-15 12:02:53 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-01-15 12:02:37 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:02:35 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:02:23 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.081 |  |
| 2026-01-15 12:02:23 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | -0.030 |  |
| 2026-01-15 12:02:21 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:02:14 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.130 |  |
| 2026-01-15 12:02:08 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:02:06 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:01:44 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:01:41 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:01:24 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:01:18 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-01-15 12:01:15 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | -0.010 |  |
| 2026-01-15 12:00:49 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:00:44 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:00:33 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-15 12:00:31 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:00:11 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | -0.011 |  |
| 2026-01-15 11:35:40 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.038 |  |
| 2026-01-15 11:34:48 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 12:12:01 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-15 12:00:33 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-15 12:03:00 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-15 12:03:54 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-15 12:01:44 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:00:31 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:00:44 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:02:35 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:01:24 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:03:21 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:00:49 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:08:16 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:02:21 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:02:06 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:05:20 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:04:34 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:02:08 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:04:09 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:03:40 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:08:49 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:05:32 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:09:55 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:02:37 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 11:02:10 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:03:29 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:01:41 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-01-15 12:12:15 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-01-15 12:01:15 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | -0.010 |  |
| 2026-01-15 12:00:11 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | -0.011 |  |
| 2026-01-15 12:01:18 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-01-15 12:02:53 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-01-15 12:04:34 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.021 |  |
| 2026-01-15 12:02:23 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | -0.030 |  |
| 2026-01-15 12:04:01 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.030 |  |
| 2026-01-15 12:07:18 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.038 |  |
| 2026-01-15 12:03:51 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.039 |  |
| 2026-01-15 12:02:23 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.081 |  |
| 2026-01-15 12:02:14 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.130 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)