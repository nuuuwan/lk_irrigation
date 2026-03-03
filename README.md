# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--03_21:20:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **88,392 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 21:20:03 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.049 |  |
| 2026-03-03 21:19:44 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:13:05 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:12:57 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:12:26 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:09:18 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:09:04 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:08:53 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-03-03 21:08:21 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.083 |  |
| 2026-03-03 21:07:53 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:07:44 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:06:55 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:06:13 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:06:04 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.028 |  |
| 2026-03-03 21:05:42 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:05:31 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | -0.019 |  |
| 2026-03-03 21:05:12 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-03 21:04:36 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:04:01 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:03:37 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:03:06 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:02:54 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:02:51 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:02:38 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:02:30 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:02:19 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-03 21:02:19 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-03-03 21:02:19 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:02:18 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:02:10 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:01:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.042 |  |
| 2026-03-03 21:01:32 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:01:25 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-03 21:01:22 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 21:01:13 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:01:10 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:00:15 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 21:05:12 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-03 21:08:53 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-03-03 21:01:25 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-03 21:01:22 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 18:08:32 | Weraganthota (Mahaweli Ganga) | -1.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-03 21:00:15 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:03:06 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:12:26 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:01:13 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:02:51 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-03 20:05:52 | Horowpothana (Yan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:02:31 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:02:30 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:07:53 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:02:38 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:12:57 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:09:04 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:19:44 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:02:54 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:02:10 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:01:10 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:02:18 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:03:37 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:06:13 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:01:32 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:13:05 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-03 18:00:53 | Thanthirimale (Malwathu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:04:01 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:04:36 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:05:42 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:07:44 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:06:55 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-03 21:02:19 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-03 21:05:31 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | -0.019 |  |
| 2026-03-03 21:02:19 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-03-03 21:06:04 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.028 |  |
| 2026-03-03 21:01:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.042 |  |
| 2026-03-03 21:20:03 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.049 |  |
| 2026-03-03 21:08:21 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.083 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)