# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_13:22:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,890 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 13:22:08 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-23 13:15:48 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:15:23 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.033 |  |
| 2026-04-23 13:11:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.92 | 🟢 Normal | -0.087 |  |
| 2026-04-23 13:11:34 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-23 13:09:56 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:09:50 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:09:38 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:08:49 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | -0.047 |  |
| 2026-04-23 13:07:56 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:07:21 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.055 |  |
| 2026-04-23 13:05:57 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.028 |  |
| 2026-04-23 13:05:57 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | -0.057 |  |
| 2026-04-23 13:05:30 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-04-23 13:05:04 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-23 13:05:04 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-23 13:04:57 | Ellagawa (Kalu Ganga) | 5.43 | 🟢 Normal | -0.029 |  |
| 2026-04-23 13:04:22 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-04-23 13:04:15 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:03:55 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:03:26 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-04-23 13:03:19 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-04-23 13:03:13 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:02:52 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:02:38 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:02:32 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:02:21 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:02:11 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:02:09 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:01:38 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:01:34 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:01:30 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 39.789 | 🔺 Rising |
| 2026-04-23 13:01:21 | Thanamalwila (Kirindi Oya) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-04-23 13:01:14 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-04-23 13:00:51 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:00:37 | Dunamale (Aththanagalu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:00:33 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 39.789 | 🔺 Rising |
| 2026-04-23 13:00:27 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-23 13:00:22 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 13:01:30 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 39.789 | 🔺 Rising |
| 2026-04-23 13:05:04 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-23 13:00:27 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-23 13:05:04 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-23 13:11:34 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-23 13:22:08 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-23 13:01:34 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:09:56 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:02:21 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:01:38 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:02:52 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:00:22 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:02:38 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:09:38 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:03:13 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:02:11 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:02:09 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:00:37 | Dunamale (Aththanagalu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:02:32 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:07:56 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:03:55 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:15:48 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:00:51 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-23 13:04:22 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-04-23 13:03:19 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-04-23 12:05:48 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | -0.011 |  |
| 2026-04-23 13:05:30 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-04-23 13:03:26 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-04-23 13:01:21 | Thanamalwila (Kirindi Oya) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-04-23 13:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-04-23 12:00:12 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-04-23 13:05:57 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.028 |  |
| 2026-04-23 13:04:57 | Ellagawa (Kalu Ganga) | 5.43 | 🟢 Normal | -0.029 |  |
| 2026-04-23 13:15:23 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.033 |  |
| 2026-04-23 13:08:49 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | -0.047 |  |
| 2026-04-23 13:07:21 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.055 |  |
| 2026-04-23 13:05:57 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | -0.057 |  |
| 2026-04-23 12:10:03 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.066 |  |
| 2026-04-23 13:11:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.92 | 🟢 Normal | -0.087 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)