# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--20_04:37:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **184,164 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 04:37:18 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:25:03 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.022 |  |
| 2026-06-20 04:22:00 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:21:59 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:21:58 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:19:27 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:19:25 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:19:24 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:16:59 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:16:43 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:14:38 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:13:13 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.008 |  |
| 2026-06-20 04:08:23 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:08:05 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:07:50 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:07:26 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-06-20 04:05:53 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-06-20 04:05:39 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-06-20 04:05:26 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:05:15 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 2.270 | 🔺 Rising |
| 2026-06-20 04:04:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.79 | 🟢 Normal | -0.028 |  |
| 2026-06-20 04:02:56 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-06-20 04:02:52 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:02:45 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.030 |  |
| 2026-06-20 04:02:43 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:02:39 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:02:37 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:02:29 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:02:21 | Dunamale (Aththanagalu Oya) | 1.59 | 🟢 Normal | -0.030 |  |
| 2026-06-20 04:02:11 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:02:09 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:01:57 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:01:22 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:01:17 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.024 |  |
| 2026-06-20 04:01:06 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-20 04:01:02 | Ellagawa (Kalu Ganga) | 5.61 | 🟢 Normal | -0.060 |  |
| 2026-06-20 04:00:57 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.001 |  |
| 2026-06-20 04:00:52 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-06-20 04:00:17 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-20 04:05:15 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 2.270 | 🔺 Rising |
| 2026-06-20 04:05:39 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-06-20 04:01:06 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-20 04:00:57 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.001 |  |
| 2026-06-20 04:02:39 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:00:15 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:00:17 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:01:22 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 02:01:42 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-19 18:02:46 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:22:00 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:16:59 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:16:43 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:02:29 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:01:57 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:02:37 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:02:09 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:02:52 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:37:18 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:08:05 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:05:26 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:14:38 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:08:23 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:02:43 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-20 04:02:11 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-20 03:03:05 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.005 |  |
| 2026-06-20 04:13:13 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.008 |  |
| 2026-06-20 04:07:26 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-06-20 04:02:56 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-06-20 04:05:53 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-06-20 04:00:52 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-06-19 18:02:43 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-20 03:13:29 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.018 |  |
| 2026-06-20 04:25:03 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.022 |  |
| 2026-06-20 04:01:17 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.024 |  |
| 2026-06-20 04:04:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.79 | 🟢 Normal | -0.028 |  |
| 2026-06-20 04:02:45 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.030 |  |
| 2026-06-20 04:02:21 | Dunamale (Aththanagalu Oya) | 1.59 | 🟢 Normal | -0.030 |  |
| 2026-06-20 04:01:02 | Ellagawa (Kalu Ganga) | 5.61 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)