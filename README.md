# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_01:08:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,579 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 01:08:19 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-03-15 01:07:47 | Dunamale (Aththanagalu Oya) | 1.25 | 🟢 Normal | -0.045 |  |
| 2026-03-15 01:06:57 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-15 01:05:55 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:04:49 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-15 01:04:42 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:04:07 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:03:57 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.036 |  |
| 2026-03-15 01:03:22 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-03-15 01:02:57 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:02:51 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:02:48 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:02:46 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.052 |  |
| 2026-03-15 01:02:33 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-03-15 01:02:30 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-15 01:02:21 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:01:33 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:01:31 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-03-15 01:01:14 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:01:06 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-15 01:00:59 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.080 |  |
| 2026-03-15 01:00:59 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-03-15 01:00:40 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-15 00:46:19 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-15 00:26:40 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-15 00:21:31 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 01:03:22 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-03-15 01:01:06 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-15 01:06:57 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-15 01:04:49 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-15 00:06:21 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-15 00:04:40 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-15 00:46:19 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-14 23:06:16 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-15 01:02:30 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-15 01:02:21 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:04:42 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-15 00:07:26 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:04:07 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:00:40 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:03:23 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-15 00:06:18 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:05:55 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:02:57 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:01:14 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:02:51 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:02:48 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-15 00:01:57 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-15 00:03:03 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 00:05:28 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:01:03 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-14 23:05:56 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:01:33 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-15 00:21:31 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.008 |  |
| 2026-03-15 01:08:19 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-03-15 01:01:31 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-03-15 00:01:41 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-03-15 01:00:59 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-03-15 01:02:33 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-03-14 22:08:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.023 |  |
| 2026-03-15 01:03:57 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.036 |  |
| 2026-03-15 01:07:47 | Dunamale (Aththanagalu Oya) | 1.25 | 🟢 Normal | -0.045 |  |
| 2026-03-15 01:02:46 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.052 |  |
| 2026-03-15 01:00:59 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.080 |  |
| 2026-03-14 18:01:50 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)