# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--21_00:56:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,920 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 00:56:31 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-21 00:50:52 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-21 00:40:34 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.071 |  |
| 2026-03-21 00:10:56 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-21 00:10:39 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.018 |  |
| 2026-03-21 00:10:31 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-21 00:09:27 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-21 00:08:43 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-03-21 00:07:12 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-03-21 00:06:55 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | -0.010 |  |
| 2026-03-21 00:06:33 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-03-21 00:05:54 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-03-21 00:05:30 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.437 | 🔺 Rising |
| 2026-03-21 00:03:59 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.030 |  |
| 2026-03-21 00:03:58 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-03-21 00:03:55 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.060 |  |
| 2026-03-21 00:03:44 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-21 00:03:22 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 00:05:30 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.437 | 🔺 Rising |
| 2026-03-21 00:01:57 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-21 00:00:13 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-21 00:10:56 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-20 18:01:37 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 00:01:44 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 00:01:51 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-21 00:02:49 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-21 00:00:27 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:01:53 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:02:58 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-21 00:56:31 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-21 00:10:31 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-21 00:01:45 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:00:43 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-21 00:03:22 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-21 00:03:44 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-20 23:03:33 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-21 00:09:27 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-21 00:01:46 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-21 00:50:52 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-21 00:02:10 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-21 00:08:43 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-03-21 00:07:12 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-03-21 00:05:54 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-03-21 00:03:58 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-03-21 00:02:22 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-03-20 23:01:36 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-03-21 00:06:55 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | -0.010 |  |
| 2026-03-20 23:02:56 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-03-21 00:06:33 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-03-21 00:10:39 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.018 |  |
| 2026-03-21 00:01:42 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | -0.020 |  |
| 2026-03-21 00:03:59 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.030 |  |
| 2026-03-20 21:08:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.039 |  |
| 2026-03-21 00:03:55 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.060 |  |
| 2026-03-21 00:40:34 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.071 |  |
| 2026-03-20 18:01:16 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.091 |  |
| 2026-03-21 00:01:38 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.186 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)