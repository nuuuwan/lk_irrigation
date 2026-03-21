# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--21_11:31:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **103,331 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 11:31:38 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:19:33 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.016 |  |
| 2026-03-21 11:15:26 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.043 |  |
| 2026-03-21 11:11:23 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.009 |  |
| 2026-03-21 11:11:19 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.009 |  |
| 2026-03-21 11:09:22 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-21 11:07:57 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-03-21 11:07:30 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:07:03 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:06:57 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-21 11:06:26 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:05:49 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:05:39 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:05:22 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:05:21 | Kithulgala (Kelani Ganga) | 1.37 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-03-21 11:05:16 | Putupaula (Kalu Ganga) | 0.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-21 11:05:08 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:05:03 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-03-21 11:04:33 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-03-21 11:03:36 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:03:33 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-21 11:03:24 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:03:06 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 11:02:52 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.070 |  |
| 2026-03-21 11:02:51 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-21 11:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | -0.050 |  |
| 2026-03-21 11:01:59 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.161 |  |
| 2026-03-21 11:01:57 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-03-21 11:01:46 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:01:44 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:01:42 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -1.012 |  |
| 2026-03-21 11:01:40 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:01:39 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:01:29 | Weraganthota (Mahaweli Ganga) | -2.08 | 🟢 Normal | -0.155 |  |
| 2026-03-21 11:01:09 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:01:01 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:01:00 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:00:50 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:00:45 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:00:18 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:59:01 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 11:05:21 | Kithulgala (Kelani Ganga) | 1.37 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-03-21 11:02:51 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-21 11:06:57 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-21 11:05:16 | Putupaula (Kalu Ganga) | 0.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-21 11:03:06 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 11:09:22 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-21 11:01:09 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:01:01 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:00:18 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:01:40 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:07:30 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:31:38 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:03:24 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:01:44 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:05:39 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:01:46 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:05:08 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:01:39 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:03:36 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:00:45 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:06:26 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:05:22 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:07:03 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:00:50 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-21 11:07:57 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-03-21 11:11:23 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.009 |  |
| 2026-03-21 11:11:19 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.009 |  |
| 2026-03-21 11:03:33 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-21 11:01:57 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-03-21 11:05:03 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-03-21 10:59:01 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-03-21 11:19:33 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.016 |  |
| 2026-03-21 11:04:33 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-03-21 11:15:26 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.043 |  |
| 2026-03-21 11:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | -0.050 |  |
| 2026-03-21 11:02:52 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.070 |  |
| 2026-03-21 11:01:29 | Weraganthota (Mahaweli Ganga) | -2.08 | 🟢 Normal | -0.155 |  |
| 2026-03-21 11:01:59 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.161 |  |
| 2026-03-21 11:01:42 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -1.012 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)