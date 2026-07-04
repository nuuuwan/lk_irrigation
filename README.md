# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_08:21:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **196,852 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 08:21:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.008 |  |
| 2026-07-04 08:16:03 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-07-04 08:16:00 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:12:19 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.009 |  |
| 2026-07-04 08:08:59 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-04 08:08:53 | Glencourse (Kelani Ganga) | 10.17 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-07-04 08:07:48 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.083 |  |
| 2026-07-04 08:07:14 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:06:53 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:06:13 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-07-04 08:06:05 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-04 08:05:55 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:05:52 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:05:40 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 08:05:18 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-07-04 08:05:05 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 08:04:53 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:04:48 | Deraniyagala (Kelani Ganga) | 2.32 | 🟢 Normal | 1.201 | 🔺 Rising |
| 2026-07-04 08:04:46 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-07-04 08:04:44 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-07-04 08:04:22 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-04 08:04:14 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:04:00 | Nawalapitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | 0.573 | 🔺 Rising |
| 2026-07-04 08:03:50 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.033 |  |
| 2026-07-04 08:03:40 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-07-04 08:03:26 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:03:01 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 08:02:42 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 08:02:35 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-07-04 08:02:01 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:01:53 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.069 |  |
| 2026-07-04 08:01:35 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-04 08:01:29 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-04 08:01:08 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-04 08:01:06 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:01:02 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:01:01 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:00:56 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-07-04 08:00:54 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.070 |  |
| 2026-07-04 08:00:22 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.043 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 08:04:46 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-07-04 08:04:48 | Deraniyagala (Kelani Ganga) | 2.32 | 🟢 Normal | 1.201 | 🔺 Rising |
| 2026-07-04 08:04:00 | Nawalapitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | 0.573 | 🔺 Rising |
| 2026-07-04 08:16:03 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-07-04 08:06:13 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-07-04 08:05:18 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-07-04 08:08:53 | Glencourse (Kelani Ganga) | 10.17 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-07-04 08:02:35 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-07-04 08:00:22 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-07-04 08:04:22 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-04 08:01:35 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-04 08:01:08 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-04 08:01:29 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-04 08:06:05 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-04 08:08:59 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-04 08:02:42 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 08:05:05 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 08:03:01 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-04 08:05:40 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 08:01:01 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:02:01 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:05:55 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:16:00 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:05:52 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:03:26 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:01:02 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:07:14 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:06:53 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:01:06 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-04 07:20:02 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:04:14 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-04 08:21:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.008 |  |
| 2026-07-04 08:12:19 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.009 |  |
| 2026-07-04 08:03:40 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-07-04 08:00:56 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-07-04 08:03:50 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.033 |  |
| 2026-07-04 08:01:53 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.069 |  |
| 2026-07-04 08:00:54 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.070 |  |
| 2026-07-04 08:07:48 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.083 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)