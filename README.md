# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--16_23:40:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **181,319 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **7** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 23:40:17 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.006 |  |
| 2026-06-16 23:15:31 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | -0.126 |  |
| 2026-06-16 23:13:14 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.060 |  |
| 2026-06-16 23:12:12 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-06-16 23:12:03 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-16 23:08:22 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-06-16 23:08:22 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.028 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 23:02:26 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-06-16 23:02:18 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-16 23:02:58 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-16 23:01:25 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-16 23:04:49 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 23:03:59 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:02:18 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-16 23:04:11 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 23:04:19 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-16 23:01:51 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:00:31 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-16 23:00:53 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 23:12:03 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-16 23:03:22 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-06-16 23:05:36 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-16 23:08:22 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-06-16 18:02:48 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-16 23:12:12 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-06-16 23:04:50 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-16 23:02:09 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-16 22:24:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.59 | 🟢 Normal | 0.000 |  |
| 2026-06-16 23:40:17 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.006 |  |
| 2026-06-16 23:06:13 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | -0.009 |  |
| 2026-06-16 23:07:07 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-06-16 23:03:39 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-16 23:03:28 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-06-16 23:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-06-16 23:02:33 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-06-16 23:06:06 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.019 |  |
| 2026-06-16 23:05:43 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-06-16 23:02:11 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.021 |  |
| 2026-06-16 23:06:34 | Panadugama (Nilwala Ganga) | 3.22 | 🟢 Normal | -0.025 |  |
| 2026-06-16 23:08:22 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.028 |  |
| 2026-06-16 23:05:41 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | -0.031 |  |
| 2026-06-16 23:05:05 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.039 |  |
| 2026-06-16 23:02:13 | Hanwella (Kelani Ganga) | 2.01 | 🟢 Normal | -0.040 |  |
| 2026-06-16 18:03:33 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.044 |  |
| 2026-06-16 23:13:14 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.060 |  |
| 2026-06-16 23:15:31 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)