# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--17_11:15:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **181,755 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 11:15:08 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:13:49 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:13:11 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.021 |  |
| 2026-06-17 11:11:25 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:09:03 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:08:19 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:07:21 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-06-17 11:06:45 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-17 11:06:20 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:06:07 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:05:38 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:05:34 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-17 11:04:18 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-06-17 11:03:59 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | -0.020 |  |
| 2026-06-17 11:03:40 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-17 11:03:33 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:03:27 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | -0.020 |  |
| 2026-06-17 11:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | -0.020 |  |
| 2026-06-17 11:03:15 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.050 |  |
| 2026-06-17 11:03:09 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 43.714 | 🔺 Rising |
| 2026-06-17 11:03:07 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:02:59 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.020 |  |
| 2026-06-17 11:02:55 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:02:55 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:02:54 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | -0.010 |  |
| 2026-06-17 11:02:41 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.029 |  |
| 2026-06-17 11:02:41 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 43.714 | 🔺 Rising |
| 2026-06-17 11:02:30 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:02:15 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:02:03 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:01:59 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:01:54 | Baddegama (Gin Ganga) | 1.61 | 🟢 Normal | -0.031 |  |
| 2026-06-17 11:01:53 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-06-17 11:01:44 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-06-17 11:01:25 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:01:16 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:00:29 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -36.000 |  |
| 2026-06-17 11:00:28 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | -36.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 11:03:09 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 43.714 | 🔺 Rising |
| 2026-06-17 11:03:40 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-17 11:06:45 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-17 11:05:34 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-17 11:01:59 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:01:16 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:02:30 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:05:38 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:13:49 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:03:07 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:15:08 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:11:25 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:08:19 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:03:33 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:02:55 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:02:15 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:06:20 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:09:03 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:02:03 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:02:55 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:06:07 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-17 11:01:25 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-17 10:03:14 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-17 10:14:45 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-06-17 11:04:18 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-06-17 11:02:54 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | -0.010 |  |
| 2026-06-17 11:07:21 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-06-17 11:01:53 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-06-17 11:01:44 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-06-17 11:03:27 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | -0.020 |  |
| 2026-06-17 11:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | -0.020 |  |
| 2026-06-17 11:03:59 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | -0.020 |  |
| 2026-06-17 11:02:59 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.020 |  |
| 2026-06-17 11:13:11 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.021 |  |
| 2026-06-17 11:02:41 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.029 |  |
| 2026-06-17 11:01:54 | Baddegama (Gin Ganga) | 1.61 | 🟢 Normal | -0.031 |  |
| 2026-06-17 10:06:27 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.038 |  |
| 2026-06-17 11:03:15 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.050 |  |
| 2026-06-17 11:00:29 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)