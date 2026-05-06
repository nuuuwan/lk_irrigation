# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_22:22:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **144,769 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 22:22:21 | Horowpothana (Yan Oya) | 2.24 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-05-06 22:14:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-05-06 22:11:08 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.065 |  |
| 2026-05-06 22:10:48 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-06 22:08:31 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-06 22:07:28 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-06 22:07:27 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-06 22:07:15 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-06 22:06:59 | Holombuwa (Kelani Ganga) | 1.49 | 🟢 Normal | 1.239 | 🔺 Rising |
| 2026-05-06 22:06:38 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.063 |  |
| 2026-05-06 22:06:35 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-05-06 22:05:33 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-05-06 22:05:10 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 22:04:40 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-06 22:04:39 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.087 |  |
| 2026-05-06 22:04:34 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-06 22:04:33 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.495 | 🔺 Rising |
| 2026-05-06 22:04:31 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 22:04:21 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.071 |  |
| 2026-05-06 22:04:13 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-06 22:04:02 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 22:03:55 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-06 22:03:02 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 22:02:48 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-05-06 22:02:43 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.010 |  |
| 2026-05-06 22:02:38 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-05-06 22:02:05 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.029 |  |
| 2026-05-06 22:02:04 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-05-06 22:01:35 | Moragaswewa (Deduru Oya) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 22:01:23 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-06 22:01:14 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-06 22:01:03 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-06 22:00:30 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-06 22:00:18 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 22:06:59 | Holombuwa (Kelani Ganga) | 1.49 | 🟢 Normal | 1.239 | 🔺 Rising |
| 2026-05-06 22:04:33 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.495 | 🔺 Rising |
| 2026-05-06 22:14:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-05-06 22:08:31 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-06 22:02:04 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-05-06 22:22:21 | Horowpothana (Yan Oya) | 2.24 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-05-06 22:03:55 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-06 22:07:15 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-06 22:07:28 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-06 22:04:13 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-06 22:01:35 | Moragaswewa (Deduru Oya) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-06 22:10:48 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-06 22:00:30 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-06 22:00:18 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 22:05:10 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 22:04:02 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 22:04:31 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 22:03:02 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 18:05:19 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 20:01:42 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 22:04:34 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-06 22:06:35 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-05-06 22:04:40 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-06 22:07:27 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-06 21:21:42 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-06 22:01:23 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-06 22:01:14 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-06 22:05:33 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:02:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:01:28 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-06 22:02:38 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-05-06 22:02:43 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.010 |  |
| 2026-05-06 22:01:03 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-06 22:02:48 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-05-06 22:02:05 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.029 |  |
| 2026-05-06 22:06:38 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.063 |  |
| 2026-05-06 22:11:08 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.065 |  |
| 2026-05-06 22:04:21 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.071 |  |
| 2026-05-06 22:04:39 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.087 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)