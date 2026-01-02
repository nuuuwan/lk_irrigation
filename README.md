# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--02_17:14:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **34,783 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 17:14:15 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.005 |  |
| 2026-01-02 17:07:59 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-01-02 17:07:46 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.113 |  |
| 2026-01-02 17:07:02 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:05:58 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.019 |  |
| 2026-01-02 17:05:54 | Padiyathalawa (Maduru Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:05:08 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-02 17:04:46 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-01-02 17:04:36 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:04:33 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:04:17 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | -0.011 |  |
| 2026-01-02 17:03:39 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:03:00 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.079 |  |
| 2026-01-02 17:02:56 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:02:46 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-01-02 17:02:45 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:02:43 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:02:18 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.279 |  |
| 2026-01-02 17:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-01-02 17:02:00 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-01-02 17:01:56 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:01:42 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.129 |  |
| 2026-01-02 17:01:41 | Siyambalanduwa (Heda Oya) | 1.26 | 🟢 Normal | -0.040 |  |
| 2026-01-02 17:01:40 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:01:35 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:01:29 | Weraganthota (Mahaweli Ganga) | -1.28 | 🟢 Normal | -0.059 |  |
| 2026-01-02 17:01:13 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.041 |  |
| 2026-01-02 17:01:07 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | -0.010 |  |
| 2026-01-02 17:00:58 | Horowpothana (Yan Oya) | 2.85 | 🟢 Normal | -0.040 |  |
| 2026-01-02 17:00:54 | Thanthirimale (Malwathu Oya) | 1.81 | 🟢 Normal | -0.032 |  |
| 2026-01-02 17:00:42 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:00:18 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:00:13 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-02 17:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:00:12 | Katharagama (Menik Ganga) | 0.40 | 🟢 Normal | -0.012 |  |
| 2026-01-02 16:42:45 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-02 16:29:49 | Padiyathalawa (Maduru Oya) | 1.35 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 17:00:13 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-02 17:05:08 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-02 16:42:45 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-02 16:15:28 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-02 17:14:15 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.005 |  |
| 2026-01-02 17:01:56 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:01:40 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:04:36 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:02:56 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:01:35 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:03:39 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:04:33 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:05:54 | Padiyathalawa (Maduru Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:02:43 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:02:45 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:00:18 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:07:02 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:18:58 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-02 16:05:53 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:00:42 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-02 17:04:46 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-01-02 17:07:59 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-01-02 17:02:00 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-01-02 17:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-01-02 17:02:46 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-01-02 17:01:07 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | -0.010 |  |
| 2026-01-02 17:04:17 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | -0.011 |  |
| 2026-01-02 17:00:12 | Katharagama (Menik Ganga) | 0.40 | 🟢 Normal | -0.012 |  |
| 2026-01-02 17:05:58 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.019 |  |
| 2026-01-02 17:00:54 | Thanthirimale (Malwathu Oya) | 1.81 | 🟢 Normal | -0.032 |  |
| 2026-01-02 17:01:41 | Siyambalanduwa (Heda Oya) | 1.26 | 🟢 Normal | -0.040 |  |
| 2026-01-02 17:00:58 | Horowpothana (Yan Oya) | 2.85 | 🟢 Normal | -0.040 |  |
| 2026-01-02 17:01:13 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.041 |  |
| 2026-01-02 17:01:29 | Weraganthota (Mahaweli Ganga) | -1.28 | 🟢 Normal | -0.059 |  |
| 2026-01-02 17:03:00 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.079 |  |
| 2026-01-02 17:07:46 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.113 |  |
| 2026-01-02 17:01:42 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.129 |  |
| 2026-01-02 17:02:18 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.279 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)