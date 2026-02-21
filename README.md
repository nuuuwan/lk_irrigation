# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_05:07:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,677 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 05:07:41 | Urawa (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.664 |  |
| 2026-02-22 05:07:06 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.009 |  |
| 2026-02-22 05:05:43 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-22 05:05:36 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-02-22 05:05:23 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | -0.041 |  |
| 2026-02-22 05:05:12 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.131 |  |
| 2026-02-22 05:05:03 | Rathnapura (Kalu Ganga) | 4.75 | 🟢 Normal | -0.103 |  |
| 2026-02-22 05:04:56 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-02-22 05:04:14 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-22 05:04:07 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-22 05:03:06 | Nakkala (Kumbukkan Oya) | 1.66 | 🟢 Normal | -0.079 |  |
| 2026-02-22 05:03:05 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-22 05:03:02 | Thawalama (Gin Ganga) | 3.35 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-22 05:02:59 | Thanamalwila (Kirindi Oya) | 2.95 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-02-22 05:02:55 | Hanwella (Kelani Ganga) | 2.51 | 🟢 Normal | 0.550 | 🔺 Rising |
| 2026-02-22 05:02:34 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-02-22 05:02:31 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.117 |  |
| 2026-02-22 05:02:25 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-22 05:02:19 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-22 05:02:16 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.052 |  |
| 2026-02-22 05:02:15 | Ellagawa (Kalu Ganga) | 7.40 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-02-22 05:02:14 | Kuda Oya (Kirindi Oya) | 2.87 | 🟢 Normal | -0.292 |  |
| 2026-02-22 05:01:50 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-22 05:01:20 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | -0.185 |  |
| 2026-02-22 05:00:45 | Manampitiya (Mahaweli Ganga) | 4.30 | 🟠 Minor Flood | 0.126 | 🔺 Rising |
| 2026-02-22 05:00:34 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-02-22 04:13:40 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-02-22 04:13:29 | Urawa (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.664 |  |
| 2026-02-22 04:12:37 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.028 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 05:00:45 | Manampitiya (Mahaweli Ganga) | 4.30 | 🟠 Minor Flood | 0.126 | 🔺 Rising |
| 2026-02-22 05:02:55 | Hanwella (Kelani Ganga) | 2.51 | 🟢 Normal | 0.550 | 🔺 Rising |
| 2026-02-22 04:02:46 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | 0.384 | 🔺 Rising |
| 2026-02-22 04:00:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-02-22 05:02:59 | Thanamalwila (Kirindi Oya) | 2.95 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-02-22 05:04:56 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-02-22 05:02:15 | Ellagawa (Kalu Ganga) | 7.40 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-02-22 05:04:14 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-22 03:02:18 | Pitabeddara (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-02-22 05:03:02 | Thawalama (Gin Ganga) | 3.35 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-22 04:06:59 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-02-22 04:05:54 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-22 04:04:22 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-22 04:12:37 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-22 05:02:25 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-22 05:04:07 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-21 18:05:22 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-22 05:00:34 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-02-22 05:02:19 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-22 05:01:50 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-22 05:03:05 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:03:47 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 05:02:34 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-02-22 05:05:43 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-22 05:07:06 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.009 |  |
| 2026-02-22 05:05:36 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-02-21 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | -0.020 |  |
| 2026-02-22 04:03:15 | Glencourse (Kelani Ganga) | 11.57 | 🟢 Normal | -0.030 |  |
| 2026-02-22 04:04:55 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.041 |  |
| 2026-02-22 05:05:23 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | -0.041 |  |
| 2026-02-22 05:02:16 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.052 |  |
| 2026-02-22 03:05:01 | Padiyathalawa (Maduru Oya) | 1.65 | 🟢 Normal | -0.053 |  |
| 2026-02-22 05:03:06 | Nakkala (Kumbukkan Oya) | 1.66 | 🟢 Normal | -0.079 |  |
| 2026-02-22 05:05:03 | Rathnapura (Kalu Ganga) | 4.75 | 🟢 Normal | -0.103 |  |
| 2026-02-22 05:02:31 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.117 |  |
| 2026-02-22 05:05:12 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.131 |  |
| 2026-02-22 05:01:20 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | -0.185 |  |
| 2026-02-22 05:02:14 | Kuda Oya (Kirindi Oya) | 2.87 | 🟢 Normal | -0.292 |  |
| 2026-02-22 05:07:41 | Urawa (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.664 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)