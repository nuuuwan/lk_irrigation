# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--05_09:23:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,169 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 09:23:53 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:12:04 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.053 |  |
| 2026-01-05 09:08:25 | Peradeniya (Mahaweli Ganga) | 2.21 | 🟢 Normal | 0.391 | 🔺 Rising |
| 2026-01-05 09:07:53 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:07:30 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-05 09:07:27 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.019 |  |
| 2026-01-05 09:06:55 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:05:40 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-01-05 09:05:15 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-05 09:05:05 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.073 |  |
| 2026-01-05 09:04:51 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.021 |  |
| 2026-01-05 09:04:31 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:04:29 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.041 |  |
| 2026-01-05 09:03:43 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-01-05 09:03:40 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | -0.019 |  |
| 2026-01-05 09:03:25 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-05 09:03:22 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.051 |  |
| 2026-01-05 09:03:22 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 09:03:12 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 09:03:00 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:02:54 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:02:51 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:02:27 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:02:18 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.021 |  |
| 2026-01-05 09:02:14 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.100 |  |
| 2026-01-05 09:02:10 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-05 09:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.080 |  |
| 2026-01-05 09:01:54 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:01:39 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | -0.025 |  |
| 2026-01-05 09:01:21 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:01:15 | Manampitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-05 09:00:53 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-01-05 09:00:48 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:00:30 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:00:28 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:00:06 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 09:08:25 | Peradeniya (Mahaweli Ganga) | 2.21 | 🟢 Normal | 0.391 | 🔺 Rising |
| 2026-01-05 08:05:02 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-05 09:01:15 | Manampitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-05 09:03:22 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 09:02:10 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-05 09:03:12 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 09:00:06 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:01:21 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:00:48 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:01:54 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:03:00 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:04:31 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:02:51 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:23:53 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:00:28 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:00:30 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:06:55 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:07:53 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:02:54 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:02:27 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-05 08:57:58 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-05 09:07:30 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-05 09:05:15 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-05 09:03:43 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-01-05 09:03:25 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-05 08:13:00 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-05 09:00:53 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-01-05 09:05:40 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-01-05 09:03:40 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | -0.019 |  |
| 2026-01-05 09:07:27 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.019 |  |
| 2026-01-05 09:04:51 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.021 |  |
| 2026-01-05 09:02:18 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.021 |  |
| 2026-01-05 09:01:39 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | -0.025 |  |
| 2026-01-05 09:04:29 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.041 |  |
| 2026-01-05 09:03:22 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.051 |  |
| 2026-01-05 09:12:04 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.053 |  |
| 2026-01-05 09:05:05 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.073 |  |
| 2026-01-05 09:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.080 |  |
| 2026-01-05 09:02:14 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)