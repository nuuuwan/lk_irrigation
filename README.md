# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--02_19:12:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,665 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-02 19:12:00 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.009 |  |
| 2025-12-02 19:09:05 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | -0.050 |  |
| 2025-12-02 19:07:02 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | -0.011 |  |
| 2025-12-02 19:07:00 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-02 19:06:12 | Giriulla (Maha Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-02 19:05:59 | Hanwella (Kelani Ganga) | 6.74 | 🟢 Normal | -0.062 |  |
| 2025-12-02 19:05:54 | Giriulla (Maha Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-02 19:05:34 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 19:05:11 | Katharagama (Menik Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2025-12-02 19:04:56 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.009 |  |
| 2025-12-02 19:04:54 | Putupaula (Kalu Ganga) | 3.57 | 🟡 Alert | -0.028 |  |
| 2025-12-02 19:04:41 | Rathnapura (Kalu Ganga) | 2.99 | 🟢 Normal | -0.100 |  |
| 2025-12-02 19:04:36 | Horowpothana (Yan Oya) | 3.78 | 🟢 Normal | -0.083 |  |
| 2025-12-02 19:04:29 | Nagalagam Street (Kelani Ganga) | 1.91 | 🟠 Minor Flood | -0.015 |  |
| 2025-12-02 19:04:23 | Nakkala (Kumbukkan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-02 19:04:03 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-02 19:03:57 | Dunamale (Aththanagalu Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2025-12-02 19:03:54 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | -0.019 |  |
| 2025-12-02 19:03:17 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-02 19:03:15 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 19:02:58 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | -0.010 |  |
| 2025-12-02 19:02:40 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-02 19:02:30 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.021 |  |
| 2025-12-02 19:02:18 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2025-12-02 19:02:10 | Ellagawa (Kalu Ganga) | 9.25 | 🟢 Normal | -0.091 |  |
| 2025-12-02 19:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-02 19:02:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.64 | 🟡 Alert | -0.050 |  |
| 2025-12-02 19:01:55 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-02 19:01:13 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-02 19:00:37 | Moraketiya (Walawe Ganga) | 1.54 | 🟢 Normal | -0.089 |  |
| 2025-12-02 19:00:37 | Thanthirimale (Malwathu Oya) | 7.97 | 🔴 Major Flood | -0.067 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-02 19:00:37 | Thanthirimale (Malwathu Oya) | 7.97 | 🔴 Major Flood | -0.067 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-02 19:04:29 | Nagalagam Street (Kelani Ganga) | 1.91 | 🟠 Minor Flood | -0.015 |  |
| 2025-12-02 19:04:54 | Putupaula (Kalu Ganga) | 3.57 | 🟡 Alert | -0.028 |  |
| 2025-12-02 19:02:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.64 | 🟡 Alert | -0.050 |  |
| 2025-12-02 19:02:40 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-02 19:01:55 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-02 19:04:23 | Nakkala (Kumbukkan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-02 19:03:15 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 19:06:12 | Giriulla (Maha Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-02 19:05:34 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 19:04:03 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:06:08 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:27:51 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:17:24 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-02 19:03:57 | Dunamale (Aththanagalu Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2025-12-02 19:07:00 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-02 19:01:13 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-02 19:03:17 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-02 19:12:00 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.009 |  |
| 2025-12-02 19:04:56 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.009 |  |
| 2025-12-02 19:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-02 19:02:18 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2025-12-02 19:05:11 | Katharagama (Menik Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2025-12-02 19:02:58 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | -0.010 |  |
| 2025-12-02 19:07:02 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | -0.011 |  |
| 2025-12-02 18:12:00 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.018 |  |
| 2025-12-02 19:03:54 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | -0.019 |  |
| 2025-12-02 19:02:30 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.021 |  |
| 2025-12-02 19:09:05 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | -0.050 |  |
| 2025-12-02 19:05:59 | Hanwella (Kelani Ganga) | 6.74 | 🟢 Normal | -0.062 |  |
| 2025-12-02 19:04:36 | Horowpothana (Yan Oya) | 3.78 | 🟢 Normal | -0.083 |  |
| 2025-12-02 19:00:37 | Moraketiya (Walawe Ganga) | 1.54 | 🟢 Normal | -0.089 |  |
| 2025-12-02 19:02:10 | Ellagawa (Kalu Ganga) | 9.25 | 🟢 Normal | -0.091 |  |
| 2025-12-02 19:04:41 | Rathnapura (Kalu Ganga) | 2.99 | 🟢 Normal | -0.100 |  |
| 2025-12-02 18:07:24 | Galgamuwa (Mee Oya) | 2.52 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)