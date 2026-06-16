# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--16_07:00:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **180,669 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **9** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 07:00:13 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 07:00:12 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-16 07:00:09 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.016 |  |
| 2026-06-16 07:00:08 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.060 |  |
| 2026-06-16 07:00:07 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 06:28:39 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.003 |  |
| 2026-06-16 06:22:58 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | -0.016 |  |
| 2026-06-16 06:13:38 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-16 06:10:05 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 06:02:48 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-06-16 06:05:54 | Panadugama (Nilwala Ganga) | 3.17 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-06-16 06:02:20 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-06-16 06:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.70 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-16 06:03:35 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-16 06:04:03 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-16 06:03:18 | Ellagawa (Kalu Ganga) | 5.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-16 06:03:13 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-16 06:01:17 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 07:00:07 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 06:13:38 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-16 06:07:51 | Hanwella (Kelani Ganga) | 2.33 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-16 06:02:56 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 06:03:37 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-16 07:00:13 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 06:04:14 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-16 06:06:53 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-16 07:00:12 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-16 06:28:39 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.003 |  |
| 2026-06-16 06:06:43 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | -0.010 |  |
| 2026-06-15 18:02:56 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-06-16 06:01:57 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-06-16 06:00:59 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-16 06:00:31 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-16 06:02:21 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-16 06:06:18 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | -0.010 |  |
| 2026-06-16 06:03:19 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-06-16 06:02:41 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-06-16 06:01:38 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-06-16 06:05:19 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.013 |  |
| 2026-06-16 07:00:09 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.016 |  |
| 2026-06-16 06:02:17 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-06-16 06:01:28 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.021 |  |
| 2026-06-16 06:00:54 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.022 |  |
| 2026-06-16 06:03:41 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | -0.030 |  |
| 2026-06-16 06:01:24 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.042 |  |
| 2026-06-16 06:03:57 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.042 |  |
| 2026-06-16 07:00:08 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.060 |  |
| 2026-06-16 06:08:22 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)