# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--07_11:20:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **199,676 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 11:20:44 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.034 |  |
| 2026-07-07 11:15:55 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.035 |  |
| 2026-07-07 11:10:10 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:09:08 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:08:36 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | -0.010 |  |
| 2026-07-07 11:07:54 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:07:50 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.009 |  |
| 2026-07-07 11:06:59 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:06:55 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:06:44 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.028 |  |
| 2026-07-07 11:05:56 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:05:45 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.031 |  |
| 2026-07-07 11:05:40 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:04:39 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:03:59 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:03:51 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-07 11:03:42 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-07-07 11:03:25 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:03:07 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-07 11:03:03 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-07-07 11:03:02 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | -0.040 |  |
| 2026-07-07 11:02:50 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-07-07 11:02:40 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-07 11:02:35 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:02:35 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.071 |  |
| 2026-07-07 11:02:33 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-07 11:02:29 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:02:24 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:02:20 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:02:13 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:02:04 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:01:54 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:01:42 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-07-07 11:01:18 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.076 |  |
| 2026-07-07 11:01:11 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:01:08 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.040 |  |
| 2026-07-07 11:01:08 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:00:10 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 10:58:47 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.035 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 11:02:50 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-07-07 11:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-07-07 11:03:07 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-07 11:03:51 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-07 11:02:40 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-07 11:02:29 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:05:40 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:04:39 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:03:42 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:00:10 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 10:05:23 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:06:59 | Magura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:05:56 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:01:08 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:09:08 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:01:54 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:03:25 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:06:55 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:02:20 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:02:13 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:02:24 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:07:54 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:01:11 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:10:10 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:03:59 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:02:35 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-07 11:07:50 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.009 |  |
| 2026-07-07 11:08:36 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | -0.010 |  |
| 2026-07-07 11:02:33 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-07-07 11:03:03 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-07-07 11:01:42 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-07-07 11:06:44 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.028 |  |
| 2026-07-07 11:05:45 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.031 |  |
| 2026-07-07 11:20:44 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.034 |  |
| 2026-07-07 11:15:55 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.035 |  |
| 2026-07-07 11:01:08 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.040 |  |
| 2026-07-07 11:03:02 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | -0.040 |  |
| 2026-07-07 11:02:35 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.071 |  |
| 2026-07-07 11:01:18 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.076 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)