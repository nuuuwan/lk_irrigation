# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--02_09:13:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **168,279 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 09:13:51 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:09:04 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-06-02 09:08:07 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:06:54 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:06:25 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 09:06:07 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | -0.021 |  |
| 2026-06-02 09:06:01 | Nagalagam Street (Kelani Ganga) | 0.11 | 🟢 Normal | -0.015 |  |
| 2026-06-02 09:05:54 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:05:18 | Rathnapura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-06-02 09:05:01 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-02 09:04:31 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | -0.012 |  |
| 2026-06-02 09:04:19 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-02 09:04:10 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.052 |  |
| 2026-06-02 09:04:07 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:04:05 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-02 09:03:57 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:03:44 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.053 |  |
| 2026-06-02 09:03:42 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-06-02 09:03:40 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-06-02 09:03:34 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.032 |  |
| 2026-06-02 09:03:30 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-02 09:03:18 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:03:05 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:02:53 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.011 |  |
| 2026-06-02 09:02:52 | Ellagawa (Kalu Ganga) | 5.21 | 🟢 Normal | -0.010 |  |
| 2026-06-02 09:02:25 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | -0.030 |  |
| 2026-06-02 09:02:07 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:01:42 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-06-02 09:01:32 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:01:30 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:01:23 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.132 |  |
| 2026-06-02 09:01:09 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:00:59 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:00:56 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:00:56 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:00:30 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:00:19 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 09:04:05 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-02 09:04:19 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-02 09:03:30 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-02 09:06:25 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 09:03:18 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:00:56 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:00:56 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:01:30 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:03:05 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:01:32 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:08:07 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:13:51 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:03:57 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:00:30 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:02:25 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:04:07 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:02:07 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:06:54 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:01:09 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:05:54 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:00:59 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-02 09:03:40 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-06-02 09:09:04 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-06-02 09:05:18 | Rathnapura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-06-02 09:02:52 | Ellagawa (Kalu Ganga) | 5.21 | 🟢 Normal | -0.010 |  |
| 2026-06-02 09:00:19 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.010 |  |
| 2026-06-02 09:01:42 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-06-02 09:05:01 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-02 09:02:53 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.011 |  |
| 2026-06-02 09:04:31 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | -0.012 |  |
| 2026-06-02 09:06:01 | Nagalagam Street (Kelani Ganga) | 0.11 | 🟢 Normal | -0.015 |  |
| 2026-06-02 09:03:42 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-06-02 09:06:07 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | -0.021 |  |
| 2026-06-02 09:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | -0.030 |  |
| 2026-06-02 09:03:34 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.032 |  |
| 2026-06-02 09:04:10 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.052 |  |
| 2026-06-02 09:03:44 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.053 |  |
| 2026-06-02 09:01:23 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.132 |  |
| 2026-06-02 08:03:27 | Manampitiya (Mahaweli Ganga) | -0.91 | 🟢 Normal | -5.571 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)