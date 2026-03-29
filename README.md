# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_04:46:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **111,118 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 04:46:52 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:39:44 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:28:26 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:21:47 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:16:50 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-30 04:13:54 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:13:52 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:13:51 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:12:21 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:08:04 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.086 |  |
| 2026-03-30 04:07:46 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-03-30 04:07:45 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.019 |  |
| 2026-03-30 04:07:08 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:05:50 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:05:50 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.409 | 🔺 Rising |
| 2026-03-30 04:05:12 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:04:08 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-30 04:04:06 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-03-30 04:03:53 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-03-30 04:03:23 | Hanwella (Kelani Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-03-30 04:03:19 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:02:47 | Ellagawa (Kalu Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:02:09 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:01:52 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:01:41 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:01:38 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:01:30 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:01:00 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-03-30 04:00:53 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-03-30 04:00:35 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.122 |  |
| 2026-03-30 04:00:09 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 04:05:50 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.409 | 🔺 Rising |
| 2026-03-30 03:05:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-03-30 04:03:53 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-03-30 03:27:56 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-30 04:16:50 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-30 04:04:08 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-30 04:07:46 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-03-30 04:00:09 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:12:21 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:01:38 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:28:26 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:39:44 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:02:09 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:01:52 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:03:02 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:13:54 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-30 03:15:27 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:02:47 | Ellagawa (Kalu Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:07:08 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-30 00:02:38 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:21:47 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:05:12 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:03:19 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:05:50 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:01:30 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-30 03:01:21 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 18:01:38 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-30 02:12:47 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:46:52 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:01:41 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-30 03:07:41 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 04:03:23 | Hanwella (Kelani Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-03-30 04:00:53 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-03-30 04:04:06 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-03-30 04:07:45 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.019 |  |
| 2026-03-30 04:01:00 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-03-30 04:08:04 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.086 |  |
| 2026-03-30 04:00:35 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.122 |  |
| 2026-03-29 18:00:53 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.229 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)