# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--02_17:31:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **168,593 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 17:31:30 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-02 17:18:00 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:15:42 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-02 17:15:30 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-02 17:13:54 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:10:24 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 17:08:44 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.011 |  |
| 2026-06-02 17:08:29 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.028 |  |
| 2026-06-02 17:08:08 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-02 17:07:57 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:07:20 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-02 17:06:54 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-06-02 17:06:21 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-02 17:06:08 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-02 17:04:44 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:04:19 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.032 |  |
| 2026-06-02 17:04:12 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 17:03:53 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:03:41 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-06-02 17:03:09 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.093 |  |
| 2026-06-02 17:03:08 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:03:03 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.010 |  |
| 2026-06-02 17:02:58 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-06-02 17:02:53 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:02:45 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | -0.022 |  |
| 2026-06-02 17:02:33 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | -0.105 |  |
| 2026-06-02 17:02:20 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 17:02:18 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:02:17 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-06-02 17:02:05 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-06-02 17:02:00 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:01:45 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:01:39 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.030 |  |
| 2026-06-02 17:01:20 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:01:20 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:01:08 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:00:19 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 17:06:54 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-06-02 17:02:58 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-06-02 17:07:20 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-02 17:06:21 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-02 17:31:30 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-02 17:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 17:10:24 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 17:04:12 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 17:06:08 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-02 17:08:08 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-02 17:15:42 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-02 17:15:30 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-02 17:02:20 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:00:19 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:01:20 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:02:00 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-02 16:16:24 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:13:54 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:01:08 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:03:08 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:18:00 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:03:53 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:01:45 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:02:18 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:02:53 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:07:57 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:01:20 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:04:44 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-02 17:03:03 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.010 |  |
| 2026-06-02 17:02:05 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-06-02 17:03:41 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-06-02 17:02:17 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-06-02 17:08:44 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.011 |  |
| 2026-06-02 17:02:45 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | -0.022 |  |
| 2026-06-02 17:08:29 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.028 |  |
| 2026-06-02 17:01:39 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.030 |  |
| 2026-06-02 17:04:19 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.032 |  |
| 2026-06-02 17:03:09 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.093 |  |
| 2026-06-02 17:02:33 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)