# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--27_18:07:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **217,835 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-27 18:07:59 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:07:21 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:06:45 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:06:36 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:05:51 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-07-27 18:05:39 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:05:21 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:05:21 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:05:03 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:04:54 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.015 |  |
| 2026-07-27 18:04:19 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-07-27 18:04:18 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:04:08 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-27 18:04:00 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:03:59 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.068 |  |
| 2026-07-27 18:03:42 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:03:31 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.066 |  |
| 2026-07-27 18:03:31 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.021 |  |
| 2026-07-27 18:03:30 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-07-27 18:03:28 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.041 |  |
| 2026-07-27 18:03:26 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-07-27 18:03:21 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:03:19 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-27 18:03:12 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:03:06 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:02:45 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-07-27 18:02:29 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:02:22 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:02:20 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | -0.010 |  |
| 2026-07-27 18:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-27 18:02:12 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:01:39 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | -0.011 |  |
| 2026-07-27 18:01:36 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.020 |  |
| 2026-07-27 18:01:22 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:01:06 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | -0.022 |  |
| 2026-07-27 18:00:39 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:00:30 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:00:10 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.074 |  |
| 2026-07-27 17:58:55 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-27 18:05:51 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-07-27 18:03:19 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-27 18:03:30 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-07-27 18:04:08 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-27 18:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-27 18:00:39 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:04:00 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:03:12 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:06:45 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:05:39 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:03:06 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:07:21 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:03:42 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:01:22 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:05:21 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:02:45 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:04:18 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:02:22 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:05:21 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:06:36 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:07:59 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:00:30 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:03:21 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-27 17:00:25 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:02:29 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:02:12 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:04:19 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-07-27 18:02:20 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | -0.010 |  |
| 2026-07-27 18:03:26 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-07-27 18:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-07-27 18:01:39 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | -0.011 |  |
| 2026-07-27 18:04:54 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.015 |  |
| 2026-07-27 18:01:36 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.020 |  |
| 2026-07-27 18:03:31 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.021 |  |
| 2026-07-27 18:01:06 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | -0.022 |  |
| 2026-07-27 18:03:28 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.041 |  |
| 2026-07-27 18:03:31 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.066 |  |
| 2026-07-27 18:03:59 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.068 |  |
| 2026-07-27 18:00:10 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)