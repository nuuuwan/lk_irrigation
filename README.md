# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_22:03:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,288 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 22:03:39 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.066 |  |
| 2026-04-13 22:03:37 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-04-13 22:03:32 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-13 22:03:19 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-13 22:03:07 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.040 |  |
| 2026-04-13 22:02:58 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-13 22:02:45 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-13 22:02:31 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.112 |  |
| 2026-04-13 22:01:34 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-13 22:01:25 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-04-13 22:01:22 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-13 22:01:22 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-13 22:01:16 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.034 |  |
| 2026-04-13 22:00:47 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 22:00:39 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-13 22:00:03 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-13 21:19:32 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-13 21:18:28 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.039 |  |
| 2026-04-13 21:15:27 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.129 |  |
| 2026-04-13 21:12:14 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 21:09:33 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-04-13 22:01:25 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-04-13 21:01:33 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-13 21:02:44 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-13 21:03:54 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-13 22:00:47 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 18:01:02 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 22:03:32 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-13 21:04:36 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 21:01:18 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 22:00:39 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:01:19 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-13 21:03:54 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-13 22:00:03 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-13 21:03:42 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-13 22:01:22 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-13 21:01:26 | Katharagama (Menik Ganga) | -0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-13 21:05:07 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-13 22:01:22 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-13 21:19:32 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-13 22:01:34 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-13 18:03:40 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.010 |  |
| 2026-04-13 22:03:19 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-13 22:03:37 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-04-13 22:02:45 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-13 22:02:58 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-13 21:01:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.029 |  |
| 2026-04-13 21:04:03 | Badalgama (Maha Oya) | 2.22 | 🟢 Normal | -0.030 |  |
| 2026-04-13 22:01:16 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.034 |  |
| 2026-04-13 21:18:28 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.039 |  |
| 2026-04-13 22:03:07 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.040 |  |
| 2026-04-13 21:05:14 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.041 |  |
| 2026-04-13 21:06:17 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.052 |  |
| 2026-04-13 22:03:39 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.066 |  |
| 2026-04-13 21:02:00 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.079 |  |
| 2026-04-13 21:00:31 | Wellawaya (Kirindi Oya) | 1.77 | 🟢 Normal | -0.080 |  |
| 2026-04-13 21:10:02 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.098 |  |
| 2026-04-13 22:02:31 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.112 |  |
| 2026-04-13 21:15:27 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)