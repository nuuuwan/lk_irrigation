# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--02_14:11:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **34,663 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 14:11:16 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:10:15 | Padiyathalawa (Maduru Oya) | 1.45 | 🟢 Normal | -0.045 |  |
| 2026-01-02 14:09:01 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-02 14:08:54 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:08:09 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:07:57 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.182 |  |
| 2026-01-02 14:07:28 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:07:05 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-02 14:05:51 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 14:05:45 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-02 14:05:42 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:03:24 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-01-02 14:02:58 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-01-02 14:02:55 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-01-02 14:02:53 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:02:52 | Galgamuwa (Mee Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-01-02 14:02:52 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:02:49 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-01-02 14:02:31 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:02:25 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 14:02:16 | Katharagama (Menik Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-01-02 14:02:11 | Horowpothana (Yan Oya) | 2.99 | 🟢 Normal | -0.079 |  |
| 2026-01-02 14:02:03 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:01:58 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:01:52 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-01-02 14:01:48 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:01:32 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-02 14:01:21 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:01:00 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:00:57 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:00:53 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-01-02 14:00:18 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-01-02 14:00:08 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-01-02 13:24:32 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-02 13:19:07 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 14:03:24 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-01-02 14:02:55 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-01-02 14:00:53 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-01-02 14:09:01 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-02 14:05:45 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-02 14:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 14:05:51 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 14:01:48 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-02 05:06:54 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:11:16 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:01:58 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:07:28 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:13:20 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:00:57 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:01:21 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:02:31 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:05:42 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:02:03 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:02:25 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:19:07 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:08:54 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:18:58 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:01:00 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-02 13:04:15 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:08:09 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:02:52 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-02 14:02:49 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-01-02 14:02:52 | Galgamuwa (Mee Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-01-02 14:07:05 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-02 14:01:32 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-02 14:00:18 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-01-02 14:02:58 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-01-02 14:01:52 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-01-02 14:00:08 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-01-02 14:02:16 | Katharagama (Menik Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-01-02 14:10:15 | Padiyathalawa (Maduru Oya) | 1.45 | 🟢 Normal | -0.045 |  |
| 2026-01-02 13:06:42 | Siyambalanduwa (Heda Oya) | 1.42 | 🟢 Normal | -0.075 |  |
| 2026-01-02 14:02:11 | Horowpothana (Yan Oya) | 2.99 | 🟢 Normal | -0.079 |  |
| 2026-01-02 14:07:57 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.182 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)