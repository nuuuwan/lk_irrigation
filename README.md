# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--26_11:10:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **162,088 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 11:10:08 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-26 11:09:33 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:09:18 | Dunamale (Aththanagalu Oya) | 2.75 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-26 11:09:06 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:08:22 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-26 11:07:51 | Magura (Kalu Ganga) | 2.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-26 11:07:50 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:06:49 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:06:26 | Rathnapura (Kalu Ganga) | 4.77 | 🟢 Normal | -0.085 |  |
| 2026-05-26 11:05:40 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:04:51 | Putupaula (Kalu Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:04:29 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:04:26 | Hanwella (Kelani Ganga) | 4.49 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-05-26 11:04:16 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:04:12 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-26 11:04:07 | Glencourse (Kelani Ganga) | 12.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-26 11:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.25 | 🟡 Alert | 0.000 |  |
| 2026-05-26 11:03:52 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-26 11:03:44 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:03:44 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:03:07 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:02:55 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-26 11:02:36 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-26 11:02:36 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.021 |  |
| 2026-05-26 11:02:15 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-26 11:02:12 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-05-26 11:02:07 | Deraniyagala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.091 |  |
| 2026-05-26 11:01:53 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:01:39 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:01:38 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-05-26 11:01:24 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.013 |  |
| 2026-05-26 11:01:20 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:01:04 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-05-26 11:00:56 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.012 |  |
| 2026-05-26 11:00:55 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:00:27 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-05-26 11:00:17 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 10:59:42 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.034 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-26 11:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.25 | 🟡 Alert | 0.000 |  |
| 2026-05-26 11:04:26 | Hanwella (Kelani Ganga) | 4.49 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-05-26 11:02:15 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-26 11:08:22 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-26 11:02:36 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-05-26 11:04:12 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-26 11:03:52 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-26 11:04:07 | Glencourse (Kelani Ganga) | 12.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-26 10:59:42 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-26 11:07:51 | Magura (Kalu Ganga) | 2.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-26 11:02:55 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-26 11:09:18 | Dunamale (Aththanagalu Oya) | 2.75 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-26 11:10:08 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-26 11:05:40 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:03:44 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:00:17 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:01:20 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:04:29 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:00:55 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:09:06 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-26 09:06:24 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:01:53 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:09:33 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:01:39 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:07:50 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:04:51 | Putupaula (Kalu Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:06:49 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:04:16 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:03:07 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:03:44 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-26 11:02:12 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-05-26 11:00:27 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-05-26 11:01:04 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-05-26 11:00:56 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.012 |  |
| 2026-05-26 11:01:24 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.013 |  |
| 2026-05-26 11:02:36 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.021 |  |
| 2026-05-26 11:01:38 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-05-26 11:06:26 | Rathnapura (Kalu Ganga) | 4.77 | 🟢 Normal | -0.085 |  |
| 2026-05-26 11:02:07 | Deraniyagala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)