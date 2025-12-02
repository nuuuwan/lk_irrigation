# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--02_18:12:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,633 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-02 18:12:00 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.018 |  |
| 2025-12-02 18:10:51 | Rathnapura (Kalu Ganga) | 3.08 | 🟢 Normal | -0.071 |  |
| 2025-12-02 18:09:33 | Ellagawa (Kalu Ganga) | 9.33 | 🟢 Normal | -0.074 |  |
| 2025-12-02 18:09:18 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-02 18:08:31 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:08:19 | Hanwella (Kelani Ganga) | 6.80 | 🟢 Normal | -0.096 |  |
| 2025-12-02 18:07:24 | Galgamuwa (Mee Oya) | 2.52 | 🟢 Normal | -0.120 |  |
| 2025-12-02 18:06:55 | Horowpothana (Yan Oya) | 3.86 | 🟢 Normal | -0.076 |  |
| 2025-12-02 18:06:31 | Thanthirimale (Malwathu Oya) | 8.03 | 🔴 Major Flood | -0.249 |  |
| 2025-12-02 18:06:08 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:06:05 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.041 |  |
| 2025-12-02 18:05:51 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:05:31 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:05:24 | Katharagama (Menik Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:04:55 | Badalgama (Maha Oya) | 3.52 | 🟢 Normal | -0.019 |  |
| 2025-12-02 18:04:21 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-02 18:04:15 | Nagalagam Street (Kelani Ganga) | 1.92 | 🟠 Minor Flood | -0.046 |  |
| 2025-12-02 18:04:07 | Katharagama (Menik Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:04:04 | Giriulla (Maha Oya) | 2.41 | 🟢 Normal | -0.045 |  |
| 2025-12-02 18:03:48 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:03:43 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:03:06 | Dunamale (Aththanagalu Oya) | 2.54 | 🟢 Normal | -0.040 |  |
| 2025-12-02 18:02:57 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:02:27 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2025-12-02 18:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.69 | 🟡 Alert | -0.051 |  |
| 2025-12-02 18:02:23 | Nakkala (Kumbukkan Oya) | 1.48 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-02 18:02:16 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:02:13 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-02 18:01:55 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:01:13 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:01:12 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-02 18:00:56 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.021 |  |
| 2025-12-02 18:00:21 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:00:10 | Putupaula (Kalu Ganga) | 3.60 | 🟡 Alert | -0.042 |  |
| 2025-12-02 17:47:13 | Thanthirimale (Malwathu Oya) | 8.11 | 🔴 Major Flood | -0.249 |  |
| 2025-12-02 17:22:27 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | 0.000 |  |
| 2025-12-02 17:22:05 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-02 18:06:31 | Thanthirimale (Malwathu Oya) | 8.03 | 🔴 Major Flood | -0.249 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-02 18:04:15 | Nagalagam Street (Kelani Ganga) | 1.92 | 🟠 Minor Flood | -0.046 |  |
| 2025-12-02 18:00:10 | Putupaula (Kalu Ganga) | 3.60 | 🟡 Alert | -0.042 |  |
| 2025-12-02 18:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.69 | 🟡 Alert | -0.051 |  |
| 2025-12-02 18:09:18 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-02 18:02:23 | Nakkala (Kumbukkan Oya) | 1.48 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-02 18:00:21 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:01:55 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:05:31 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:03:48 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:03:43 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:06:08 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-02 17:22:27 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:17:24 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:08:31 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | 0.000 |  |
| 2025-12-02 17:06:26 | Moraketiya (Walawe Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:05:24 | Katharagama (Menik Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:02:57 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:02:16 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-02 18:02:13 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-02 18:04:21 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-02 18:01:12 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-02 18:02:27 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2025-12-02 17:14:37 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | -0.016 |  |
| 2025-12-02 18:12:00 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.018 |  |
| 2025-12-02 18:04:55 | Badalgama (Maha Oya) | 3.52 | 🟢 Normal | -0.019 |  |
| 2025-12-02 18:00:56 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.021 |  |
| 2025-12-02 18:03:06 | Dunamale (Aththanagalu Oya) | 2.54 | 🟢 Normal | -0.040 |  |
| 2025-12-02 18:06:05 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.041 |  |
| 2025-12-02 18:04:04 | Giriulla (Maha Oya) | 2.41 | 🟢 Normal | -0.045 |  |
| 2025-12-02 18:10:51 | Rathnapura (Kalu Ganga) | 3.08 | 🟢 Normal | -0.071 |  |
| 2025-12-02 18:09:33 | Ellagawa (Kalu Ganga) | 9.33 | 🟢 Normal | -0.074 |  |
| 2025-12-02 18:06:55 | Horowpothana (Yan Oya) | 3.86 | 🟢 Normal | -0.076 |  |
| 2025-12-02 18:08:19 | Hanwella (Kelani Ganga) | 6.80 | 🟢 Normal | -0.096 |  |
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

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)