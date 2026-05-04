# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_15:09:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **142,748 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 15:09:55 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:08:34 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:08:09 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-04 15:07:49 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-04 15:06:04 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:06:03 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:05:50 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:05:42 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:05:18 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.019 |  |
| 2026-05-04 15:04:49 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-05-04 15:04:32 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.020 |  |
| 2026-05-04 15:04:23 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-05-04 15:03:50 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-05-04 15:03:34 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:03:25 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-05-04 15:03:22 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.035 |  |
| 2026-05-04 15:03:07 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-05-04 15:03:02 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:02:51 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:02:34 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:02:33 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.061 |  |
| 2026-05-04 15:02:30 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-04 15:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-05-04 15:02:15 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:01:49 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.051 |  |
| 2026-05-04 15:01:42 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:01:35 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:01:27 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:01:26 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.030 |  |
| 2026-05-04 15:01:21 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:01:13 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:01:06 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-05-04 15:00:49 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-05-04 15:00:49 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:00:49 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:00:45 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 14:02:45 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-04 15:02:30 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-04 15:08:09 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-04 15:01:27 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:01:35 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:05:42 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:02:34 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:00:45 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:01:21 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:06:04 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:08:34 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:00:49 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:03:34 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:09:55 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:01:44 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:05:50 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:02:51 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:02:15 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:03:02 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:01:13 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:00:49 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:01:42 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:04:52 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:06:03 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-04 15:07:49 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-04 15:04:49 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-05-04 15:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-05-04 15:03:25 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-05-04 15:00:49 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-05-04 15:04:23 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-05-04 15:05:18 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.019 |  |
| 2026-05-04 15:03:07 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-05-04 15:04:32 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.020 |  |
| 2026-05-04 15:01:06 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-05-04 15:03:50 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-05-04 15:01:26 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.030 |  |
| 2026-05-04 15:03:22 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.035 |  |
| 2026-05-04 15:01:49 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.051 |  |
| 2026-05-04 15:02:33 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)