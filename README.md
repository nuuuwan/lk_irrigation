# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_08:36:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **139,811 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 08:36:11 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:36:10 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:36:08 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:28:49 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.035 |  |
| 2026-05-01 08:08:36 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-05-01 08:08:23 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-01 08:07:18 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | -0.019 |  |
| 2026-05-01 08:06:53 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:06:39 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:06:37 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:06:20 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | -0.011 |  |
| 2026-05-01 08:06:17 | Rathnapura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.098 |  |
| 2026-05-01 08:06:11 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.051 |  |
| 2026-05-01 08:06:04 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-05-01 08:05:57 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-05-01 08:05:31 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-05-01 08:05:12 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:05:09 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | -0.049 |  |
| 2026-05-01 08:03:32 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.100 |  |
| 2026-05-01 08:03:22 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-05-01 08:03:15 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-05-01 08:03:15 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-01 08:03:07 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:02:56 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:02:52 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | -0.099 |  |
| 2026-05-01 08:02:29 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-01 08:02:24 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-05-01 08:02:17 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:02:13 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:02:13 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-05-01 08:02:07 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:02:04 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-05-01 08:01:37 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | -0.020 |  |
| 2026-05-01 08:01:35 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 08:01:25 | Thanthirimale (Malwathu Oya) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:01:09 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:01:06 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:00:55 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-01 08:00:34 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | -0.032 |  |
| 2026-05-01 08:00:15 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 08:00:55 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-01 08:03:15 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-01 08:02:29 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-01 08:01:35 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 08:01:09 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:02:17 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:00:15 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:02:13 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:06:39 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:02:56 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:36:11 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:06:53 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:02:07 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:06:37 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:01:06 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:02:52 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:05:12 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:01:25 | Thanthirimale (Malwathu Oya) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:03:07 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-01 08:05:31 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-05-01 08:03:15 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-05-01 08:08:23 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-01 08:02:13 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-05-01 08:02:24 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-05-01 08:05:57 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-05-01 08:03:22 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-05-01 08:08:36 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-05-01 08:06:20 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | -0.011 |  |
| 2026-05-01 08:07:18 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | -0.019 |  |
| 2026-05-01 08:06:04 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-05-01 08:01:37 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | -0.020 |  |
| 2026-05-01 08:02:04 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-05-01 08:00:34 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | -0.032 |  |
| 2026-05-01 08:28:49 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.035 |  |
| 2026-05-01 08:05:09 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | -0.049 |  |
| 2026-05-01 08:06:11 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.051 |  |
| 2026-05-01 08:06:17 | Rathnapura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.098 |  |
| 2026-05-01 08:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | -0.099 |  |
| 2026-05-01 08:03:32 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)