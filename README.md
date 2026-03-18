# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--19_03:22:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **101,229 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 03:22:22 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-19 03:17:51 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-19 03:10:20 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 03:09:29 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-19 03:08:29 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-03-19 03:07:47 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:07:41 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.042 |  |
| 2026-03-19 03:06:41 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.201 |  |
| 2026-03-19 03:05:26 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.005 |  |
| 2026-03-19 03:04:53 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-19 03:04:51 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-19 03:04:48 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 2.000 | 🔺 Rising |
| 2026-03-19 03:04:00 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:03:44 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | -0.012 |  |
| 2026-03-19 03:03:35 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:03:21 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 2.000 | 🔺 Rising |
| 2026-03-19 03:03:13 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-03-19 03:02:59 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:02:57 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-19 03:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 2.000 | 🔺 Rising |
| 2026-03-19 03:02:43 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:02:42 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:02:29 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-03-19 03:02:28 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:02:22 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.140 |  |
| 2026-03-19 03:02:20 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:02:17 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:02:14 | Manampitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-19 03:02:08 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-19 03:02:00 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:01:57 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:01:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | 2.000 | 🔺 Rising |
| 2026-03-19 03:01:38 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:01:10 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:00:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 2.000 | 🔺 Rising |
| 2026-03-19 03:00:41 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.051 |  |
| 2026-03-19 02:53:31 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.042 |  |
| 2026-03-19 02:52:11 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 03:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 2.000 | 🔺 Rising |
| 2026-03-19 03:08:29 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-03-19 03:09:29 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-18 23:04:23 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-19 03:02:57 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-19 03:02:08 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-19 03:02:14 | Manampitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-19 03:10:20 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 03:04:53 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-19 03:17:51 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-19 03:22:22 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-19 03:05:26 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.005 |  |
| 2026-03-19 03:02:17 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:02:43 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:01:38 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:02:28 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:01:57 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 18:02:16 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:07:47 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:04:48 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:04:00 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:02:42 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:52:11 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-19 02:02:46 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:02:20 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:03:21 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:03:35 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-18 18:02:03 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:02:00 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-19 03:03:13 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-03-19 03:04:51 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-19 03:02:29 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-03-19 03:03:44 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | -0.012 |  |
| 2026-03-19 02:05:36 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-03-19 03:07:41 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.042 |  |
| 2026-03-19 03:00:41 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.051 |  |
| 2026-03-18 18:02:41 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.088 |  |
| 2026-03-19 03:02:22 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.140 |  |
| 2026-03-19 03:06:41 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.201 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)