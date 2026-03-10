# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--10_10:22:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **94,254 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 10:22:08 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.008 |  |
| 2026-03-10 10:16:25 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.025 |  |
| 2026-03-10 10:12:31 | Moraketiya (Walawe Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:11:13 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.057 |  |
| 2026-03-10 10:09:22 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:05:55 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:05:46 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-03-10 10:05:40 | Thawalama (Gin Ganga) | 0.93 | 🟢 Normal | -0.019 |  |
| 2026-03-10 10:05:38 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:05:35 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-03-10 10:05:28 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | -0.086 |  |
| 2026-03-10 10:04:58 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:04:04 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:03:44 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-10 10:03:41 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:03:26 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | 0.530 | 🔺 Rising |
| 2026-03-10 10:03:21 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.060 |  |
| 2026-03-10 10:03:08 | Dunamale (Aththanagalu Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:03:01 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.173 |  |
| 2026-03-10 10:02:48 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:02:47 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:02:47 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.060 |  |
| 2026-03-10 10:02:41 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:02:37 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-03-10 10:02:36 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:02:34 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 2.038 | 🔺 Rising |
| 2026-03-10 10:02:12 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-10 10:02:05 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:02:01 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | -0.010 |  |
| 2026-03-10 10:01:53 | Badalgama (Maha Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:01:41 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 2.038 | 🔺 Rising |
| 2026-03-10 10:01:34 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-03-10 10:01:33 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.030 |  |
| 2026-03-10 10:01:26 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-03-10 10:01:17 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:01:09 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.031 |  |
| 2026-03-10 10:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:00:58 | Putupaula (Kalu Ganga) | 0.26 | 🟢 Normal | -0.061 |  |
| 2026-03-10 10:00:47 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 10:02:34 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 2.038 | 🔺 Rising |
| 2026-03-10 10:03:26 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | 0.530 | 🔺 Rising |
| 2026-03-10 10:02:12 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-10 10:03:44 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-10 10:01:17 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:03:41 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:02:47 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:00:47 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:09:22 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:02:36 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:05:55 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:03:21 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:12:31 | Moraketiya (Walawe Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:02:05 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:03:08 | Dunamale (Aththanagalu Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:02:48 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:01:53 | Badalgama (Maha Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:04:58 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:05:38 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:04:04 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:02:41 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-10 10:22:08 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.008 |  |
| 2026-03-10 10:05:35 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-03-10 10:01:26 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-03-10 10:02:01 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | -0.010 |  |
| 2026-03-10 10:05:46 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-03-10 10:01:34 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-03-10 10:02:37 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-03-10 10:05:40 | Thawalama (Gin Ganga) | 0.93 | 🟢 Normal | -0.019 |  |
| 2026-03-10 10:16:25 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.025 |  |
| 2026-03-10 10:01:33 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.030 |  |
| 2026-03-10 10:01:09 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.031 |  |
| 2026-03-10 10:11:13 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.057 |  |
| 2026-03-10 10:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.060 |  |
| 2026-03-10 10:02:47 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.060 |  |
| 2026-03-10 10:00:58 | Putupaula (Kalu Ganga) | 0.26 | 🟢 Normal | -0.061 |  |
| 2026-03-10 10:05:28 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | -0.086 |  |
| 2026-03-10 10:03:01 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.173 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)