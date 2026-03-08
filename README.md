# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--08_06:14:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **92,291 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 06:14:41 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:14:34 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:11:25 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.473 |  |
| 2026-03-08 06:10:33 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-08 06:09:48 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:08:31 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:08:29 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.087 |  |
| 2026-03-08 06:08:09 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:07:09 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:06:56 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:04:49 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:04:32 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:04:07 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 06:03:49 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:03:43 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-08 06:03:37 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.020 |  |
| 2026-03-08 06:03:35 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.252 |  |
| 2026-03-08 06:03:16 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:03:06 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:02:59 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:02:53 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.332 |  |
| 2026-03-08 06:02:47 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | -0.013 |  |
| 2026-03-08 06:02:45 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:02:44 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.019 |  |
| 2026-03-08 06:02:39 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.059 |  |
| 2026-03-08 06:02:30 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:02:26 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.030 |  |
| 2026-03-08 06:02:21 | Weraganthota (Mahaweli Ganga) | -1.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-08 06:02:17 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:02:15 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:01:44 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:01:38 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:01:35 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 06:00:59 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:00:46 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:59:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.332 |  |
| 2026-03-08 05:38:21 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-08 05:34:59 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.252 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 05:03:17 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-03-08 06:02:21 | Weraganthota (Mahaweli Ganga) | -1.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-08 06:03:43 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-08 06:04:07 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 06:01:35 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 06:10:33 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-08 06:01:38 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:00:46 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:02:17 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:02:30 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:08:31 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:02:53 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:02:36 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:02:15 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:14:41 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:03:49 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:03:16 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:09:48 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:14:34 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:04:32 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:08:09 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:01:44 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:02:59 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:02:45 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:04:49 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:06:56 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:07:09 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:00:59 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:02:19 | Thanthirimale (Malwathu Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:03:06 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-08 06:02:47 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | -0.013 |  |
| 2026-03-08 06:02:44 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.019 |  |
| 2026-03-08 06:03:37 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.020 |  |
| 2026-03-08 06:02:26 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.030 |  |
| 2026-03-08 06:02:39 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.059 |  |
| 2026-03-08 06:08:29 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.087 |  |
| 2026-03-08 06:03:35 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.252 |  |
| 2026-03-08 06:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.332 |  |
| 2026-03-08 06:11:25 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.473 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)