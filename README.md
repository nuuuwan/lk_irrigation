# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_07:09:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **112,114 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 07:09:07 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:08:36 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:07:41 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-31 07:07:31 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-03-31 07:07:00 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-03-31 07:06:09 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.012 |  |
| 2026-03-31 07:05:59 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:05:55 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:05:43 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-31 07:05:12 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.114 |  |
| 2026-03-31 07:05:07 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-03-31 07:04:31 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | -0.049 |  |
| 2026-03-31 07:04:27 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:03:51 | Hanwella (Kelani Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-03-31 07:03:36 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 07:03:32 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:03:25 | Baddegama (Gin Ganga) | 0.79 | 🟢 Normal | -0.052 |  |
| 2026-03-31 07:03:21 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:03:19 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 07:03:14 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 07:03:04 | Weraganthota (Mahaweli Ganga) | -1.96 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-03-31 07:02:50 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:02:38 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:02:36 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-31 07:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.064 |  |
| 2026-03-31 07:02:10 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:02:08 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | -0.005 |  |
| 2026-03-31 07:02:06 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:02:02 | Peradeniya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.053 |  |
| 2026-03-31 07:01:34 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-03-31 07:01:18 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.034 |  |
| 2026-03-31 07:01:14 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:01:01 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:33:04 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:29:51 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:21:48 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 07:03:04 | Weraganthota (Mahaweli Ganga) | -1.96 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-03-31 07:05:43 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-31 07:02:36 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-31 07:03:36 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 07:03:14 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 07:03:19 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 07:07:41 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-31 07:08:36 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:01:14 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:04:27 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:00:46 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:02:06 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:09:07 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:03:21 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:02:38 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:01:34 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:02:50 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:02:38 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:05:55 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:02:10 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:03:32 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:04:16 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:01:01 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-31 06:29:51 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:05:59 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-31 07:02:08 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | -0.005 |  |
| 2026-03-31 06:12:40 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | -0.009 |  |
| 2026-03-31 07:07:31 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-03-31 07:03:51 | Hanwella (Kelani Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-03-31 07:07:00 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-03-31 07:06:09 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.012 |  |
| 2026-03-31 07:05:07 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-03-31 07:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-03-31 07:01:18 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.034 |  |
| 2026-03-31 07:04:31 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | -0.049 |  |
| 2026-03-31 07:03:25 | Baddegama (Gin Ganga) | 0.79 | 🟢 Normal | -0.052 |  |
| 2026-03-31 07:02:02 | Peradeniya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.053 |  |
| 2026-03-31 07:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.064 |  |
| 2026-03-31 07:05:12 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.114 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)