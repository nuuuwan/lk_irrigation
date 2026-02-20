# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--20_19:13:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **78,421 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 19:13:00 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-20 19:12:12 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-20 19:10:56 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.051 |  |
| 2026-02-20 19:09:03 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:08:44 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:06:44 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-20 19:06:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-02-20 19:06:06 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-20 19:05:45 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:05:43 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.019 |  |
| 2026-02-20 19:05:32 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:05:07 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-20 19:04:47 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:04:14 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.019 |  |
| 2026-02-20 19:04:09 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:03:48 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:03:36 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.060 |  |
| 2026-02-20 19:03:12 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-20 19:03:00 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:02:55 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.040 |  |
| 2026-02-20 19:02:46 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.022 |  |
| 2026-02-20 19:02:36 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:02:29 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-20 19:02:27 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-02-20 19:02:01 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-20 19:01:55 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:01:46 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-20 19:01:44 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:01:37 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:01:35 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:01:24 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-20 19:00:53 | Manampitiya (Mahaweli Ganga) | 3.08 | 🟡 Alert | 0.061 | 🔺 Rising |
| 2026-02-20 19:00:53 | Padiyathalawa (Maduru Oya) | 1.90 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-20 19:00:50 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-20 19:00:32 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-02-20 19:00:11 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:33:00 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 19:00:53 | Manampitiya (Mahaweli Ganga) | 3.08 | 🟡 Alert | 0.061 | 🔺 Rising |
| 2026-02-20 19:00:53 | Padiyathalawa (Maduru Oya) | 1.90 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-20 19:06:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-02-20 19:13:00 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-20 19:01:46 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-20 19:12:12 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-20 19:06:06 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-20 19:02:29 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-20 19:01:24 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-20 19:02:01 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-20 19:06:44 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-20 19:05:07 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-20 19:00:50 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-20 19:03:12 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-20 19:09:03 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:01:44 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:01:55 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:01:35 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:03:00 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:00:11 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:04:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:04:47 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:05:45 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:08:44 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:02:36 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:04:09 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:05:32 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:01:33 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:01:37 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-20 19:00:32 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-02-20 19:05:43 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.019 |  |
| 2026-02-20 19:04:14 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.019 |  |
| 2026-02-20 19:02:27 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-02-20 19:02:46 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.022 |  |
| 2026-02-20 18:11:51 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.026 |  |
| 2026-02-20 19:02:55 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.040 |  |
| 2026-02-20 18:02:20 | Weraganthota (Mahaweli Ganga) | -1.32 | 🟢 Normal | -0.051 |  |
| 2026-02-20 19:10:56 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.051 |  |
| 2026-02-20 19:03:36 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)