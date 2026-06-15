# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--16_01:19:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **180,490 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 01:19:46 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:14:43 | Rathnapura (Kalu Ganga) | 2.00 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-16 01:09:42 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-06-16 01:08:25 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-16 01:07:28 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-16 01:07:00 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.019 |  |
| 2026-06-16 01:06:09 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:06:00 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:05:56 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-06-16 01:05:45 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-06-16 01:05:30 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.009 |  |
| 2026-06-16 01:05:29 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:04:39 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:04:21 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:03:54 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:03:49 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 01:03:47 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:03:44 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 01:03:28 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:02:52 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:02:36 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:02:33 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:02:17 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-16 01:02:09 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | -0.020 |  |
| 2026-06-16 01:01:22 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:01:12 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.176 |  |
| 2026-06-16 01:01:10 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | -0.010 |  |
| 2026-06-16 01:00:17 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-16 00:56:22 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-16 00:49:41 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 00:03:58 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-06-16 01:14:43 | Rathnapura (Kalu Ganga) | 2.00 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-16 01:08:25 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-16 01:02:17 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-16 01:07:28 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-16 01:03:44 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 01:03:49 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-15 18:03:40 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:00:17 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:03:54 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:02:36 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:03:28 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:02:33 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:02:52 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-16 00:04:35 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:05:29 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:03:47 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:04:21 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:06:09 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:19:46 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:01:22 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-15 22:04:58 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-16 00:04:01 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:04:39 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:06:00 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-16 01:05:30 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.009 |  |
| 2026-06-16 01:09:42 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-06-15 18:02:56 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-06-16 01:05:45 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-06-16 01:01:10 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | -0.010 |  |
| 2026-06-16 01:05:56 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-06-16 00:28:12 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | -0.014 |  |
| 2026-06-16 01:07:00 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.019 |  |
| 2026-06-16 01:02:09 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | -0.020 |  |
| 2026-06-15 23:06:09 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | -0.021 |  |
| 2026-06-15 18:00:33 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | -0.026 |  |
| 2026-06-15 23:05:38 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.049 |  |
| 2026-06-15 23:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | -0.090 |  |
| 2026-06-16 01:01:12 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.176 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)