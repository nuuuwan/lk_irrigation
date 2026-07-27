# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--27_09:27:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **217,482 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-27 09:27:53 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:22:14 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:11:57 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-07-27 09:09:15 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | -0.026 |  |
| 2026-07-27 09:09:02 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-27 09:08:06 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-07-27 09:07:24 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | -0.011 |  |
| 2026-07-27 09:07:15 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:05:50 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:05:21 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:04:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.079 |  |
| 2026-07-27 09:04:06 | Thalgahagoda (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.049 |  |
| 2026-07-27 09:04:06 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:03:43 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-07-27 09:03:42 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-27 09:03:33 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:03:33 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:03:27 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.096 |  |
| 2026-07-27 09:03:25 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:03:23 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.078 |  |
| 2026-07-27 09:03:22 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.053 |  |
| 2026-07-27 09:03:15 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:03:07 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:02:45 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:02:40 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:02:40 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:02:39 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:02:30 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:02:27 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-27 09:02:21 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-07-27 09:02:15 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:02:09 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:01:51 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:01:50 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:01:23 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-27 09:01:21 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:01:14 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:00:59 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-27 09:03:43 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-07-27 09:01:23 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-27 09:03:42 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-27 09:02:27 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-27 09:09:02 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-27 09:02:15 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:07:15 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:01:50 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:01:21 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:27:53 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:22:14 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:05:50 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:02:39 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:02:45 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:03:25 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:04:06 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:01:51 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:03:33 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:00:59 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:02:40 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:03:07 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:03:15 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:05:21 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:02:30 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:02:40 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-07-27 08:00:30 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-27 08:16:26 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:01:14 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:02:09 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-27 09:08:06 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-07-27 09:07:24 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | -0.011 |  |
| 2026-07-27 09:11:57 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-07-27 09:02:21 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-07-27 09:09:15 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | -0.026 |  |
| 2026-07-27 09:04:06 | Thalgahagoda (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.049 |  |
| 2026-07-27 09:03:22 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.053 |  |
| 2026-07-27 09:03:23 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.078 |  |
| 2026-07-27 09:04:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.079 |  |
| 2026-07-27 09:03:27 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)