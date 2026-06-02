# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--02_14:18:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **168,476 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 14:18:44 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:16:15 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-02 14:16:14 | Moragaswewa (Deduru Oya) | 0.33 | 🟢 Normal | -0.008 |  |
| 2026-06-02 14:11:03 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.009 |  |
| 2026-06-02 14:08:35 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | -0.009 |  |
| 2026-06-02 14:08:27 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 14:08:14 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-06-02 14:06:28 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:06:23 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:06:18 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:06:09 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:06:07 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-02 14:06:04 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:05:30 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-06-02 14:04:58 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-02 14:04:39 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:03:40 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:03:16 | Hanwella (Kelani Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-06-02 14:03:04 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:02:47 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:02:43 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-02 14:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.010 |  |
| 2026-06-02 14:02:34 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:02:33 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-02 14:02:31 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-06-02 14:02:16 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:02:09 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:02:08 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:01:59 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:01:58 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:01:54 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:01:44 | Glencourse (Kelani Ganga) | 9.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 14:01:30 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:01:12 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:00:56 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-02 14:00:27 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:00:24 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-06-02 14:00:17 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:00:10 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:00:07 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 14:05:30 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-06-02 14:02:31 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-06-02 14:06:07 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-02 14:16:15 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-02 14:02:33 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-02 14:04:58 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-02 14:00:56 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-02 14:01:44 | Glencourse (Kelani Ganga) | 9.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 14:08:27 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 14:00:17 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:02:09 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:00:10 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:02:47 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:01:59 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:01:58 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:02:16 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:00:27 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:03:40 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:01:12 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:06:04 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-02 13:07:22 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:01:30 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:00:07 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:02:34 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:02:08 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:06:28 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:06:18 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:01:54 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:18:44 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:06:09 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:06:23 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 14:16:14 | Moragaswewa (Deduru Oya) | 0.33 | 🟢 Normal | -0.008 |  |
| 2026-06-02 14:08:35 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | -0.009 |  |
| 2026-06-02 14:11:03 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.009 |  |
| 2026-06-02 14:08:14 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-06-02 14:02:43 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-02 14:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.010 |  |
| 2026-06-02 14:03:16 | Hanwella (Kelani Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-06-02 14:00:24 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | -0.010 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)