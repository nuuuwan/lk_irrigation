# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_13:19:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,150 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 13:19:54 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-14 13:13:25 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:11:04 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.027 |  |
| 2026-03-14 13:09:09 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.018 |  |
| 2026-03-14 13:07:57 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:07:40 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:07:31 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-03-14 13:07:15 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-14 13:07:12 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.037 |  |
| 2026-03-14 13:07:12 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:06:45 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:06:15 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.019 |  |
| 2026-03-14 13:05:28 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.019 |  |
| 2026-03-14 13:04:13 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-14 13:04:01 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | -0.069 |  |
| 2026-03-14 13:03:52 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-14 13:03:22 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-03-14 13:03:21 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.040 |  |
| 2026-03-14 13:02:54 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:02:36 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2026-03-14 13:02:35 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-14 13:02:31 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.120 |  |
| 2026-03-14 13:02:29 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-14 13:02:14 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-14 13:02:06 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:01:59 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-03-14 13:01:57 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:01:50 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:01:47 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:01:26 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:01:16 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.022 |  |
| 2026-03-14 13:01:09 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-03-14 13:01:02 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:00:59 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:00:52 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:00:39 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:00:38 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.011 |  |
| 2026-03-14 13:00:18 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 13:04:13 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-14 13:01:09 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-03-14 13:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-14 13:03:52 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-14 13:02:35 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-14 13:02:14 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-14 13:19:54 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-14 13:00:18 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-14 13:07:15 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-14 13:07:40 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:01:02 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:00:52 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:01:50 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:07:57 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:01:26 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:02:06 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:07:12 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:01:57 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:02:54 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:02:29 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:13:25 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:00:59 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:06:45 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-14 13:01:47 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-14 12:03:07 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.006 |  |
| 2026-03-14 13:07:31 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-03-14 13:01:59 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-03-14 13:00:38 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.011 |  |
| 2026-03-14 13:09:09 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.018 |  |
| 2026-03-14 13:05:28 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.019 |  |
| 2026-03-14 13:06:15 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.019 |  |
| 2026-03-14 13:03:22 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-03-14 13:02:36 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2026-03-14 13:01:16 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.022 |  |
| 2026-03-14 13:11:04 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.027 |  |
| 2026-03-14 13:07:12 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.037 |  |
| 2026-03-14 13:03:21 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.040 |  |
| 2026-03-14 13:04:01 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | -0.069 |  |
| 2026-03-14 13:02:31 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)