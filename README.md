# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--06_21:09:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **65,973 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 21:09:19 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:08:55 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-02-06 21:08:39 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:05:43 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:05:39 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.058 |  |
| 2026-02-06 21:05:06 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-06 21:04:33 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-02-06 21:04:28 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:04:27 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:04:14 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.111 |  |
| 2026-02-06 21:04:11 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:04:05 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:03:52 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:03:52 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:03:30 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:03:10 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-06 21:02:36 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.055 |  |
| 2026-02-06 21:02:31 | Horowpothana (Yan Oya) | 3.12 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-02-06 21:02:27 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 21:02:20 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-06 21:02:17 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:02:10 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-06 21:02:03 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-02-06 21:02:02 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:01:54 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:01:48 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-02-06 21:00:38 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:00:27 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.042 |  |
| 2026-02-06 21:00:07 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-02-06 20:42:17 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-06 21:01:48 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-02-06 21:04:33 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-06 21:00:07 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-02-06 21:08:55 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-02-06 21:02:31 | Horowpothana (Yan Oya) | 3.12 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-02-06 21:03:10 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-06 20:05:20 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-02-06 21:05:06 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-06 21:02:10 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-06 21:02:27 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-06 21:01:54 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:00:38 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:03:30 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:03:52 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:04:57 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:09:19 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:08:58 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:03:52 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:42:17 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:04:27 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:05:43 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:02:17 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:04:11 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:04:28 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:08:39 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:03:13 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:02:29 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:02:02 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:04:05 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-06 20:10:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-02-06 21:02:20 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-06 21:02:03 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-02-06 18:01:44 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | -0.039 |  |
| 2026-02-06 21:00:27 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.042 |  |
| 2026-02-06 21:02:36 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.055 |  |
| 2026-02-06 21:05:39 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.058 |  |
| 2026-02-06 21:04:14 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)