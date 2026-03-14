# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_07:30:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,916 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 07:30:12 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.007 |  |
| 2026-03-14 07:22:31 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-14 07:21:24 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.023 |  |
| 2026-03-14 07:19:29 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.016 |  |
| 2026-03-14 07:18:02 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-03-14 07:16:54 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.017 |  |
| 2026-03-14 07:14:47 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-03-14 07:10:10 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.016 |  |
| 2026-03-14 07:09:51 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-14 07:07:03 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.456 | 🔺 Rising |
| 2026-03-14 07:06:37 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-14 07:06:37 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-03-14 07:06:17 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.140 |  |
| 2026-03-14 07:05:58 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-14 07:05:14 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 07:05:09 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | 0.000 |  |
| 2026-03-14 07:04:44 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-14 07:04:26 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 07:03:58 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-14 07:03:49 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.071 |  |
| 2026-03-14 07:03:16 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-14 07:03:15 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 07:02:59 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-03-14 07:02:27 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.097 |  |
| 2026-03-14 07:02:17 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.039 |  |
| 2026-03-14 07:02:12 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 07:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | -0.157 |  |
| 2026-03-14 07:01:50 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 07:01:42 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | 0.000 |  |
| 2026-03-14 07:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-03-14 07:01:39 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.072 |  |
| 2026-03-14 07:01:38 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-14 07:01:35 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 07:01:30 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-14 07:01:20 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.110 |  |
| 2026-03-14 07:01:08 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.042 |  |
| 2026-03-14 07:01:05 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.002 |  |
| 2026-03-14 07:00:19 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-03-14 07:00:16 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 07:07:03 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.456 | 🔺 Rising |
| 2026-03-14 07:03:16 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-14 07:06:37 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-14 07:03:58 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-14 07:01:38 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-14 07:04:44 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-14 07:03:15 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 07:18:02 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-03-14 07:14:47 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-03-14 07:02:12 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 07:05:58 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-14 07:01:05 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.002 |  |
| 2026-03-14 07:00:16 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 07:01:50 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 07:01:35 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 07:22:31 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-14 07:05:09 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | 0.000 |  |
| 2026-03-14 07:04:26 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 07:05:14 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 07:09:51 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-14 07:01:30 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-14 07:30:12 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.007 |  |
| 2026-03-14 07:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-03-14 07:00:19 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-03-14 07:02:59 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-03-14 07:10:10 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.016 |  |
| 2026-03-14 07:19:29 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.016 |  |
| 2026-03-14 07:16:54 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.017 |  |
| 2026-03-14 07:06:37 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-03-14 07:21:24 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.023 |  |
| 2026-03-14 07:02:17 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.039 |  |
| 2026-03-14 07:01:08 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.042 |  |
| 2026-03-14 07:03:49 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.071 |  |
| 2026-03-14 07:01:39 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.072 |  |
| 2026-03-14 07:02:27 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.097 |  |
| 2026-03-14 06:00:54 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.099 |  |
| 2026-03-14 07:01:20 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.110 |  |
| 2026-03-14 07:06:17 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.140 |  |
| 2026-03-14 07:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | -0.157 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)