# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--12_13:25:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **95,368 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 13:25:50 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-03-12 13:16:44 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:15:02 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:13:44 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:13:27 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:11:34 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.053 |  |
| 2026-03-12 13:07:56 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-03-12 13:06:53 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-12 13:06:27 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:06:25 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.018 |  |
| 2026-03-12 13:06:08 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-12 13:05:33 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:05:06 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-03-12 13:04:00 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-03-12 13:03:43 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:03:23 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:03:17 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:03:15 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:03:15 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-03-12 13:03:13 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | -0.051 |  |
| 2026-03-12 13:03:08 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:02:50 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-03-12 13:02:39 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:02:38 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:02:36 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.062 |  |
| 2026-03-12 13:02:20 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:02:19 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:02:10 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:01:49 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:01:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | -0.041 |  |
| 2026-03-12 13:00:55 | Weraganthota (Mahaweli Ganga) | -2.49 | 🟢 Normal | -0.090 |  |
| 2026-03-12 13:00:54 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-12 13:00:44 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:00:36 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.040 |  |
| 2026-03-12 13:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 13:04:00 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-03-12 13:06:53 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-12 12:12:54 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-12 13:06:08 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-12 13:25:50 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-03-12 13:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 13:02:39 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:03:15 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 12:02:32 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:02:10 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:01:49 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:03:43 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:00:44 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:16:44 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:15:02 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:02:19 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:03:08 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:06:27 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:13:27 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:13:44 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 12:05:52 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:03:17 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:05:33 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:03:23 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-12 12:01:47 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:02:38 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:02:20 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-12 13:05:06 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-03-12 13:02:50 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-03-12 13:07:56 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-03-12 13:03:15 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-03-12 13:00:54 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-12 13:06:25 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.018 |  |
| 2026-03-12 13:00:36 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.040 |  |
| 2026-03-12 13:01:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | -0.041 |  |
| 2026-03-12 13:03:13 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | -0.051 |  |
| 2026-03-12 13:11:34 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.053 |  |
| 2026-03-12 13:02:36 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.062 |  |
| 2026-03-12 13:00:55 | Weraganthota (Mahaweli Ganga) | -2.49 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)