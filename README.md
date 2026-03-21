# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--21_08:12:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **103,209 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 08:12:36 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:10:15 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:09:45 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.005 |  |
| 2026-03-21 08:09:09 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.206 |  |
| 2026-03-21 08:07:56 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.014 |  |
| 2026-03-21 08:07:49 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.077 |  |
| 2026-03-21 08:06:34 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-03-21 08:06:33 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:05:42 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.019 |  |
| 2026-03-21 08:05:26 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:05:16 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-21 08:05:13 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.013 |  |
| 2026-03-21 08:04:55 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:04:39 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.094 |  |
| 2026-03-21 08:04:32 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-21 08:04:15 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-03-21 08:04:00 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-03-21 08:03:45 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:03:42 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-03-21 08:03:42 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:03:32 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-21 08:03:23 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:03:14 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:03:13 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:03:10 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.099 |  |
| 2026-03-21 08:02:34 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:02:32 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:02:32 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 08:02:25 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.031 |  |
| 2026-03-21 08:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | -0.080 |  |
| 2026-03-21 08:02:05 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:02:02 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:01:58 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:01:49 | Weraganthota (Mahaweli Ganga) | -2.31 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-21 08:01:44 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:01:38 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:01:15 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-03-21 08:01:15 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.010 |  |
| 2026-03-21 08:01:13 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 08:01:49 | Weraganthota (Mahaweli Ganga) | -2.31 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-21 08:05:16 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-21 08:03:32 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-21 08:04:32 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-21 08:02:32 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 08:09:45 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.005 |  |
| 2026-03-21 08:01:58 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:03:23 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:10:15 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:03:13 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:02:34 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:04:55 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:02:32 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:02:05 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:03:45 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:03:14 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:06:33 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:05:26 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:02:02 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:03:42 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:01:44 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:12:36 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:01:38 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-21 08:04:00 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-03-21 08:04:15 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-03-21 08:01:15 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-03-21 08:01:15 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.010 |  |
| 2026-03-21 08:05:13 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.013 |  |
| 2026-03-21 08:07:56 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.014 |  |
| 2026-03-21 08:05:42 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.019 |  |
| 2026-03-21 08:06:34 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-03-21 08:03:42 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-03-21 08:01:13 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | -0.030 |  |
| 2026-03-21 08:02:25 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.031 |  |
| 2026-03-21 08:07:49 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.077 |  |
| 2026-03-21 08:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | -0.080 |  |
| 2026-03-21 08:04:39 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.094 |  |
| 2026-03-21 08:03:10 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.099 |  |
| 2026-03-21 08:09:09 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.206 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)