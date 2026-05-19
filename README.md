# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_10:15:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **155,982 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 10:15:32 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.035 |  |
| 2026-05-19 10:11:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.88 | 🟢 Normal | -0.057 |  |
| 2026-05-19 10:10:41 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-19 10:07:49 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:07:44 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:07:18 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-19 10:07:11 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-05-19 10:06:53 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:06:45 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:06:31 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:06:31 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.047 |  |
| 2026-05-19 10:06:12 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.021 |  |
| 2026-05-19 10:06:01 | Thanthirimale (Malwathu Oya) | 2.40 | 🟢 Normal | -0.028 |  |
| 2026-05-19 10:05:16 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | -0.030 |  |
| 2026-05-19 10:05:12 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:04:55 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-05-19 10:04:36 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.019 |  |
| 2026-05-19 10:04:35 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-05-19 10:04:28 | Hanwella (Kelani Ganga) | 1.99 | 🟢 Normal | -0.039 |  |
| 2026-05-19 10:04:26 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.011 |  |
| 2026-05-19 10:04:13 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:04:05 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:03:42 | Galgamuwa (Mee Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:03:41 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:03:30 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-05-19 10:03:08 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-19 10:02:57 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:02:27 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:02:14 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:02:12 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:02:08 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | -0.013 |  |
| 2026-05-19 10:01:53 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:01:46 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-19 10:01:18 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-19 10:01:12 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:01:10 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:01:05 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:01:02 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -0.022 |  |
| 2026-05-19 10:00:53 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:00:06 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.060 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 10:01:18 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-19 10:07:18 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-19 10:01:46 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-19 10:10:41 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-19 10:03:08 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-19 10:00:53 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:02:57 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:06:31 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:04:05 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:03:42 | Galgamuwa (Mee Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:01:12 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:02:14 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:07:49 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:03:41 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:05:12 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:07:44 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:01:10 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:02:27 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:04:13 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:06:45 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:06:53 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:01:53 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:01:05 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-19 10:07:11 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-05-19 10:04:35 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-05-19 10:04:26 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.011 |  |
| 2026-05-19 10:02:08 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | -0.013 |  |
| 2026-05-19 10:04:36 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.019 |  |
| 2026-05-19 10:03:30 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-05-19 10:04:55 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-05-19 10:06:12 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.021 |  |
| 2026-05-19 10:01:02 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -0.022 |  |
| 2026-05-19 10:06:01 | Thanthirimale (Malwathu Oya) | 2.40 | 🟢 Normal | -0.028 |  |
| 2026-05-19 10:05:16 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | -0.030 |  |
| 2026-05-19 10:15:32 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.035 |  |
| 2026-05-19 10:04:28 | Hanwella (Kelani Ganga) | 1.99 | 🟢 Normal | -0.039 |  |
| 2026-05-19 10:06:31 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.047 |  |
| 2026-05-19 10:11:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.88 | 🟢 Normal | -0.057 |  |
| 2026-05-19 10:00:06 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)